from .util import Token, Symbol, SymbolTable, default_value
from .lang import cml_grammar, cml_table


def parse_syntax(tokens: list[Token], empty="^", verbose=False):
    stack: list[str] = ["0"]
    tk_input: list[Token] = [t for t in tokens if t.name != "unknown"]
    tk_input.append(Token(name="$", value="$", file="", pos="", span=-1))
    actions: list[str] = []

    tk_read: list[Token] = []
    tk_errors: list[Token] = []

    result = True

    symbol_table = SymbolTable()
    symbol_stack: list[Symbol] = []
    cur_stack: list[Token] = []
    code_buffer: list[str] = []

    while True:
        cur_input = tk_input[0]
        cur_state = stack[-1]

        action = cml_table[cur_state][cur_input.name]
        actions.append(action)

        if action == "e":
            result = False
            stack = ["0"]
            tk_errors.append(tk_input.pop(0))
            continue

        if action == "acc":
            break

        if action[0] == "s":  # stack
            if verbose:
                print(f'stacked {cur_input}')
            tk_read.append(tk_input.pop(0))
            cur_stack.append(tk_read[-1])

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

            # parse semantics
            if verbose:
                print(r_rule)

            match r_rule:
                case {"head": "STMTS'", "body": ["STMTS"]}: ...
                case {"head": "STMTS", "body": ["^"]}:
                    symbol_table.openScope()
                case {"head": "STMTS", "body": ["STMTS", "STMT"]}: ...
                case {"head": "STMT", "body": ["ATTRIB_STMT", ";"]}: ...
                case {"head": "STMT", "body": ["FLOW"]}: ...
                case {"head": "STMT", "body": ["DECL_STMT", ";"]}: ...
                case {"head": "STMT", "body": ["COMMAND", ";"]}: ...
                case {"head": "DECL_STMT", "body": ["type", "id", "DECL_END"]}:
                    # add variable to symbol table
                    cur_symbol = symbol_stack.pop()
                    symbol_table.insert(cur_symbol)
                    code_buffer.append(f'{cur_symbol.name} = {cur_symbol.value} ;')
                    cur_stack = []
                case {"head": "DECL_END", "body": ["^"]}:
                    print(f'{cur_stack=}')
                    _type = cur_stack[0]
                    _id = cur_stack[1]
                    symbol_stack.append(Symbol(
                        name=_id.value,
                        type=_type.value,
                        value=default_value[_type.value],
                    ))
                    print(f'{symbol_stack=}')
                case {"head": "DECL_END", "body": ["attrib", "EXPR"]}: ...
                case {"head": "ATTRIB_STMT", "body": ["id", "ATTRIB_END"]}: ...
                case {"head": "ATTRIB_END", "body": ["attrib", "EXPR"]}: ...
                case {"head": "ATTRIB_END", "body": ["attrib_op", "EXPR"]}: ...
                case {"head": "EXPR", "body": ["BOOL_EXPR"]}: ...
                case {"head": "BOOL_EXPR", "body": ["not", "EXPR"]}: ...
                case {"head": "BOOL_EXPR", "body": ["REL_EXPR", "BOOL_EXPR_C"]}: ...
                case {"head": "BOOL_EXPR_C", "body": ["^"]}: ...
                case {"head": "BOOL_EXPR_C", "body": ["bool_op", "REL_EXPR"]}: ...
                case {"head": "REL_EXPR", "body": ["ARITH_EXPR", "REL_EXPR_C"]}: ...
                case {"head": "REL_EXPR_C", "body": ["^"]}: ...
                case {"head": "REL_EXPR_C", "body": ["rel_op", "ARITH_EXPR"]}: ...
                case {"head": "ARITH_EXPR", "body": ["TERM", "ARITH_EXPR_C"]}: ...
                case {"head": "ARITH_EXPR_C", "body": ["arith_op_sum", "TERM"]}: ...
                case {"head": "ARITH_EXPR_C", "body": ["^"]}: ...
                case {"head": "TERM", "body": ["FACTOR", "TERM_C"]}: ...
                case {"head": "TERM_C", "body": ["arith_op_mul", "FACTOR"]}: ...
                case {"head": "TERM_C", "body": ["^"]}: ...
                case {"head": "FACTOR", "body": ["(", "EXPR", ")"]}: ...
                case {"head": "FACTOR", "body": ["VALUE"]}: ...
                case {"head": "FLOW", "body": ["WHILE_STMT"]}: ...
                case {"head": "FLOW", "body": ["IF_STMT"]}: ...
                case {"head": "FLOW", "body": ["FOR_STMT"]}: ...
                case {"head": "IF_STMT", "body": ["if", "(", "BOOL_EXPR", ")", "{", "STMTS", "}", "ELSE_STMT"]}: ...
                case {"head": "ELSE_STMT", "body": ["else", "{", "STMTS", "}"]}: ...
                case {"head": "ELSE_STMT", "body": ["^"]}: ...
                case {"head": "WHILE_STMT", "body": ["while", "(", "BOOL_EXPR", ")", "{", "STMTS", "}"]}: ...
                case {"head": "FOR_STMT", "body": ["for", "(", "DECL_STMT", ";", "BOOL_EXPR", ";", "ATTRIB_STMT", ")", "{", "STMTS", "}"]}: ...
                case {"head": "COMMAND", "body": ["read", "id"]}: ...
                case {"head": "COMMAND", "body": ["write", "VALUE", "WCHAIN"]}: ...
                case {"head": "WCHAIN", "body": ["^"]}: ...
                case {"head": "WCHAIN", "body": [", ", "VALUE", "WCHAIN"]}: ...
                case {"head": "VALUE", "body": ["LITERAL"]}: ...
                case {"head": "VALUE", "body": ["id"]}: ...
                case {"head": "LITERAL", "body": ["literal_int"]}: ...
                case {"head": "LITERAL", "body": ["literal_float"]}: ...
                case {"head": "LITERAL", "body": ["literal_bool"]}: ...
                case {"head": "LITERAL", "body": ["literal_str"]}: ...

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

    # code_buffer: list[str] = []

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
        if token:
            if token.name == "id":
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

                consume("attrib")
                expr()
                consume(";")
        else:
            consume("UNKNOWN")

    def expr():
        # Verifica se as variáveis nos dois lados do operador '=' têm o mesmo tipo
        left_var = consume("id")
        consume("attrib")
        right_var = consume("id")

        if left_var and right_var:
            left_symbol = symbol_table.lookup(left_var.value)
            right_symbol = symbol_table.lookup(right_var.value)

            if left_symbol and right_symbol and left_symbol.type != right_symbol.type:
                print(
                    f"[error:sem] Tentativa de atribuição entre variáveis de tipos diferentes: {left_var.value} ({left_symbol.type}) e {right_var.value} ({right_symbol.type})"
                )

    program()  # Inicia o processo de análise    # Grammar rules for CML
