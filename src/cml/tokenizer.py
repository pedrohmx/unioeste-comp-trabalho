# lexer

import re
# from pprint import pprint as pp
from .util import Rule, Token


def tokenize(source: str, rules: list[Rule], filename: str = ''):
    regex = '|'.join(f'(?P<{x.name}>{x.pattern})' for x in rules)
    aliases = {x.name: x.alias for x in rules if x.alias}

    pos: int = 0
    line: int = 1
    line_start: int = 0

    tokens: list[Token] = []

    for match in re.finditer(regex, source):
        token_name = match.lastgroup
        if token_name is None:
            print('-'*64)
            print(match)
            print('-'*64)
            continue

        token_lexeme = match.group(token_name)
        if token_name in aliases:
            token_name = aliases[token_name]

        if token_name in ['newline', 'comment']:
            line_start = match.end()
            line += 1
            continue
        if token_name == 'ws':
            continue

        pos = match.start() - line_start

        if token_name == 'literal_int':
            if '0x' in token_lexeme:
                value = str(int(token_lexeme, 16))
            elif '0o' in token_lexeme:
                value = str(int(token_lexeme, 8))
            elif '0b' in token_lexeme:
                value = str(int(token_lexeme, 2))
            else:
                value = token_lexeme
        else:
            value = token_lexeme

        tok = Token(
            name=token_name,
            value=value,
            file=filename,
            pos=f':{line}:{pos+1}',
            span=match.end() - match.start()
        )

        tokens.append(tok)
    return tokens
