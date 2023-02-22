from .util import Token

grammar: dict = {}

def parse_syntax(tokens: list[Token]):
    # load table
    
    # stacks
    stack: list[int|str] = [0]
    input: list[str] = [t.name for t in tokens]
    input.append("$")
    actions: list[str] = []
    
    while True:
        cur_input = input[0]
        cur_stack = stack[-1]
        
        table_line = grammar[cur_input]
        action = table_line[cur_stack]
        actions.append(action)
        
        if action == 'ACC':
            return True
        
        if action[0] == 's':  # stack
            input.pop(0)
            
            stack.append(cur_input)
            stack.append(action[1:])
        elif action[0] == 'r':  # reduce
            # search reduce rule
            rr = find_reduction_rule(int(action[1:]))
            # apply reduction
            rs = get_reduction_size(rr)
            # change state
            ns = ...
            # add current state to stack
            stack.append(...) # append reduction non terminal
            stack.append(ns)
        else:  # ???
            raise ValueError("Invalid action")


# stubs
def find_reduction_rule(i: int) -> dict: ...
def get_reduction_size(d: dict) -> int: ...
