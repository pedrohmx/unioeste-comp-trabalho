from .util import Token
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
