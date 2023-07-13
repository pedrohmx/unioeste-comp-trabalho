from dataclasses import dataclass
from typing import TypedDict


class GrammarRule(TypedDict):
    head: str
    body: list[str]


@dataclass
class Rule:
    name:    str
    pattern: str
    alias:   str | None = None


@dataclass
class Token:
    name:  str
    value: str
    file:  str
    pos:   str
    span:  int

    def __repr__(self):
        return f'< {self.file + self.pos} | {self.name} | {self.value} >'
