#!/usr/bin/env python3

from pathlib import Path
from typer import Typer

from .lexer import tokenize, Token
from .rules import cml_rules

app = Typer(no_args_is_help=True)

@app.command('lex', no_args_is_help=True)
def lex(source: Path):
    '''
    Tokenize source code.
    '''
    if not source.exists():
        print("Source file does not exists, exiting.")
        raise SystemExit(1)
    tokens: list[Token]
    with open(source, 'r') as f:
        tokens = tokenize(f.read(), cml_rules, source.name)
    for t in tokens:
        print(t)


@app.command('parse', no_args_is_help=True)
def parse(source: Path):
    '''
    Not implemented yet.
    '''
    print('Not implemented yet.')
    raise SystemExit(1)

if __name__ == '__main__':
    app()