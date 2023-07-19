from dataclasses import dataclass, field
from typing import TypedDict, TypeAlias, Any


class GrammarRule(TypedDict):
    head: str
    body: list[str]


@dataclass
class Rule:
    name: str
    pattern: str
    alias: str | None = None


@dataclass
class Token:
    name: str
    value: str
    file: str
    pos: str
    span: int

    def __repr__(self):
        return f"<{self.file + self.pos} | {self.name} | {self.value}>"


@dataclass
class Node:
    node_type: str
    value: Any
    children: list["Node"] = field(default_factory=list)

    def __repr__(self) -> str:
        if self.children:
            children_str = ", ".join(repr(child) for child in self.children)
            return f"Node({self.node_type}, [{children_str}])"
        elif self.value is not None:
            return f"Node({self.node_type}, value={self.value})"
        else:
            return f"Node({self.node_type})"


@dataclass
class Symbol:
    name: str
    type: str
    value: Any
    scope: int

    def __repr__(self) -> str:
        return f"[{self.name}] type={self.type} scope={self.scope}"


Scope: TypeAlias = dict[str, Symbol]


class SymbolTable:
    scope_list: list[Scope]
    scopes: list[Scope]
    scope_count: int = 0

    def __init__(self):
        self.scopes = []
        self.scope_list = []

    def insert(self, symbol: Symbol):
        cur_scope = self.scopes[::-1][0]
        if symbol.name not in cur_scope:
            symbol.scope = self.scope_count - 1
            cur_scope[symbol.name] = symbol
        else:
            print("Symbol already in scope")
            print(f"{symbol=}")
            print(f"{cur_scope=}")

    def lookup(self, name: str) -> Symbol | None:
        for scope in self.scopes[::-1]:
            if name in scope:
                return scope[name]
        return None

    def openScope(self):
        self.scope_count += 1
        new_scope = dict()
        self.scopes.append(new_scope)
        self.scope_list.append(new_scope)

    def closeScope(self):
        self.scopes.pop()

    def destroy(self):
        ...


# S-Attr
