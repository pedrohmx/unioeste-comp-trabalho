#!/usr/bin/env python3

from pathlib import Path
from typer import Typer
from rich.console import Console
from rich.text import Text
from rich.table import Table

from .lexer import tokenize, Token
from .lang import cml_res

app = Typer(no_args_is_help=True)

@app.command('lex', no_args_is_help=True)
def lex(source: Path, color: bool = False):
    '''
    Tokenize source code.
    '''
    if not source.exists():
        print("Source file does not exists, exiting.")
        raise SystemExit(1)
    tokens: list[Token]
    with open(source, 'r') as f:
        tokens = tokenize(f.read(), cml_res, source.name)

    console = Console()
    
    grid = Table.grid(padding=(0, 5))

    grid.add_column()
    grid.add_column(justify="right")
    grid.add_column(justify="right")

    if color:
        for t in tokens:
            warn = t.name == 'unknown'
            grid.add_row(
                Text.assemble((t.file, 'gray'),(t.pos, 'green' if not warn else 'yellow')),
                Text(t.name, 'green' if not warn else 'red'),
                Text(t.value, 'blue' if not warn else 'red')
            )
    else:
        for t in tokens:
            grid.add_row(
                f'{t.file}{t.pos}',
                t.name,
                t.value
            )
    console.print(grid)


@app.command('parse', no_args_is_help=True)
def parse(source: Path):
    '''
    Not implemented yet.
    '''
    print('Not implemented yet.')
    raise SystemExit(1)

if __name__ == '__main__':
    app()
