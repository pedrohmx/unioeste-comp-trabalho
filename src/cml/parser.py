from .util import Token, Symbol, SymbolTable
from .lang import cml_grammar, cml_table


def parse_syntax(tokens: list[Token], empty="^"):
    stack: list[str] = ["0"]
    # tk_input: list[str] = [t.name for t in tokens if t.name != "unknown"]
    tk_input: list[Token] = [t for t in tokens if t.name != "unknown"]
    tk_input.append(Token(name="$", value="$", file="", pos="", span=-1))
    actions: list[str] = []

    tk_read: list[Token] = []
    tk_errors: list[Token] = []

    result = True

    while True:
        cur_input = tk_input[0]
        cur_state = stack[-1]

        # print(f"> stack: {stack}")
        # print(f"> input: {input}")
        # print(f"> actions: {actions}")
        # print(f"> cur input: {cur_input}")
        # print(f"> cur state: {cur_state}")

        action = cml_table[cur_state][cur_input.name]
        actions.append(action)

        if action == "e":
            result = False
            # print('[ERROR]: parsing error')
            # print(f'> {stack=}')
            # print(f'> {cur_input}')
            # strategy 1 - clear stack
            stack = ["0"]
            tk_errors.append(tk_input.pop(0))
            continue
            # # change to warn and consume the error
            # # fixme: do a proper implementation after finithing the reduction
            # raise ValueError("Parser reached an invalid state and is throwing an error :(")

        if action == "acc":
            break

        if action[0] == "s":  # stack
            tk_read.append(tk_input.pop(0))

            stack.append(cur_input.name)
            stack.append(action[1:])

        elif action[0] == "r":  # reduce
            # search reduce rule
            r_rule = cml_grammar[int(action[1:])]

            # get size to reduce
            r_size = 0
            if r_rule["body"] and r_rule["body"][0] != empty:
                r_size = len(r_rule["body"]) * 2

            # reduce stack
            if r_size:
                stack = stack[:-r_size]

            # change state
            next_state = goto_lookup(index=stack[-1], symbol=r_rule["head"])
            if next_state == "e":
                print(f"Goto Error when index={stack[-1]} and symbol={r_rule['head']}")

            # append reduction non terminal
            stack.append(r_rule["head"])
            # add current state to stack
            stack.append(next_state)
        else:
            raise ValueError("Invalid action")
        # print("-"*64)
    return result, tk_read, tk_errors


def goto_lookup(index: int | str, symbol: str) -> str:
    try:
        i = str(index)
        res = cml_table[i][symbol]
        return res
    except Exception as e:
        print(e)
    return ""


def parse_semantics(in_tokens: list[Token]):
    tokens = in_tokens[::-1]

    # Tabela de símbolos para variáveis
    symbol_table = SymbolTable()

    # Função auxiliar para obter o próximo token sem consumi-lo
    def peek() -> Token | None:
        return tokens[-1] if tokens else None

    # Função auxiliar para consumir um token esperado
    def consume(expected_token_type: str) -> Token | None:
        token = peek()
        if token and token.name == expected_token_type:
            return tokens.pop()
        else:
            print(
                f'[error:sem] Esperado "{expected_token_type}", encontrado "{token.name if token else None}"'
            )
            raise ValueError(
                f'[error:sem] Esperado "{expected_token_type}", encontrado "{token.name if token else None}"'
            )
            return None

    code_buffer: list[str] = []

    # Regras semanticas

    def program():
        stmts()
        # Destrói a tabela de símbolos quando a análise estiver completa
        symbol_table.destroy()

    def stmts():
        next_token = peek()
        while next_token and next_token.name != "$":
            stmt()

    # analisa um único comando ou declaração
    def stmt():
        token = peek()
        if token and token.name == "id":
            if temp := consume(token.name):
                var_name = temp.value
            else:
                raise ValueError(f"Found {temp} while searching for {token}")

            # Verifica se a variável já foi declarada
            if symbol_table.lookup(var_name) is None:
                # Insere a variável na tabela de símbolos com escopo global (0)
                symbol_table.insert(
                    Symbol(name=var_name, type="unknown", value=None, scope=0)
                )
            else:
                print(f'[error:sem] Variável "{var_name}" já foi declarada.')
                # raise ValueError(f'[error:sem] Variável "{var_name}" já foi declarada.')

            consume("=")
            expr()
            consume(";")
        else:
            consume("UNKNOWN")

    def expr():
        # Verifica se as variáveis nos dois lados do operador '=' têm o mesmo tipo
        left_var = consume("id")
        consume("=")
        right_var = consume("id")

        if left_var and right_var:
            left_symbol = symbol_table.lookup(left_var.value)
            right_symbol = symbol_table.lookup(right_var.value)

            if left_symbol and right_symbol and left_symbol.type != right_symbol.type:
                print(
                    f"[error:sem] Tentativa de atribuição entre variáveis de tipos diferentes: {left_var.value} ({left_symbol.type}) e {right_var.value} ({right_symbol.type})"
                )

    program()  # Inicia o processo de análise    # Grammar rules for CML
