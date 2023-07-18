#!/usr/bin/env python3

from pathlib import Path
from typer import Typer
from rich.console import Console
from rich.text import Text
from rich.table import Table

from .tokenizer import tokenize, Token
from .parser import parse_syntax
from .lang import cml_rules

app = Typer(no_args_is_help=True)


@app.command(no_args_is_help=True)
def compile(source: Path, output: str = "cml.3addr.txt"):
    """Compiles from source file"""
    if not source.exists():
        print("[error:comp] Source file does not exists, exiting.")
        raise SystemExit(1)

    tokens: list[Token]
    with open(source, "r") as f:
        tokens = tokenize(f.read(), cml_rules, source.name)

    lex_error = False
    for token in tokens:
        if token.name == "unknown":
            print(f"[error:lex] @ {token}")
            lex_error = True
    if lex_error:
        print("[error:comp] halting...")
        raise SystemExit(1)
    else:
        print("[info:comp] lex ok.")

    parse_result, ok, err = parse_syntax(tokens=tokens)
    if parse_result:
        print("[info:comp] parse ok.")
    else:
        print("[error:parse] halting...")
        print("[error:parse] errors @")
        for e in err:
            print(e)


@app.command("lex", no_args_is_help=True)
def lex(source: Path, color: bool = False):
    """
    Tokenize source code.
    """
    if not source.exists():
        print("Source file does not exists, exiting.")
        raise SystemExit(1)
    tokens: list[Token]
    with open(source, "r") as f:
        tokens = tokenize(f.read(), cml_rules, source.name)

    console = Console()

    grid = Table.grid(padding=(0, 5))

    grid.add_column()
    grid.add_column(justify="right")
    grid.add_column(justify="right")

    if color:
        for t in tokens:
            warn = t.name == "unknown"
            grid.add_row(
                Text.assemble(
                    (t.file, "gray"), (t.pos, "green" if not warn else "yellow")
                ),
                Text(t.name, "green" if not warn else "red"),
                Text(t.value, "blue" if not warn else "red"),
            )
    else:
        for t in tokens:
            grid.add_row(f"{t.file}{t.pos}", t.name, t.value)
    console.print(grid)


@app.command("parse", no_args_is_help=True)
def parse(source: Path):
    """parse syntax"""
    if not source.exists():
        print("Source file does not exists, exiting.")
        raise SystemExit(1)
    tokens: list[Token]
    with open(source, "r") as f:
        tokens = tokenize(f.read(), cml_rules, source.name)

    result, ok, err = parse_syntax(tokens=tokens)
    if result:
        print("Syntax ok")
    else:
        print("Error parsing syntax.")
        print("Obs: Some errors only occurs due to previous errors.")
        print("Unexpected tokens at:")
        for token in err:
            print(token)
    raise SystemExit(0)


if __name__ == "__main__":
    app()
