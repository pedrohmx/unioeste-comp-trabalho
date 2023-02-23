from .util import Token
from .lang import grammar_dev, slr_table

def parse_syntax(tokens: list[Token]):
    stack: list[int | str] = [0]
    input: list[str] = [t.name for t in tokens]
    input.append("$")
    actions: list[str | int] = []

    while True:
        cur_input = input[0]
        cur_state = stack[-1]

        table_line = slr_table[cur_input]

        action = str(table_line[int(cur_state)])  # type:ignore
        actions.append(action)
        
        if action == 'e':
            raise ValueError("Parser reached an invalid state and is throwing an error :(")

        if action == 'ACC':
            return True

        if action[0] == 's':  # stack
            input.pop(0)

            stack.append(cur_input)
            stack.append(int(action[1:]))
        
        elif action[0] == 'r':  # reduce            
            # search reduce rule
            rr = grammar_dev[int(action[1:])]
            
            # get size to reduce
            rs = len(rr['dev']) * 2
            
            # change state
            next_state = goto_lookup(index=stack[-1], symbol=rr['nonterm'])
            # if 'e' in next_state:
            #     raise ValueError("Invalid goto")
            
            # append reduction non terminal
            stack.append(rr['nonterm'])  # type:ignore
            # add current state to stack
            stack.append(int(next_state))  # type:ignore
        else:  # ???
            raise ValueError("Invalid action")
    return False


def goto_lookup(index, symbol):
    try:
        i = int(index)
        res = slr_table[symbol][i]
        return res
    except Exception as e:
        print(e)
