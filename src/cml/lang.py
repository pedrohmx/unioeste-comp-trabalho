import os
import json
from .util import Rule, GrammarRule

cml_grammar: list[GrammarRule] = json.load(
    open(os.path.join(os.path.dirname(__file__), "grammar.json"))
)

# cml_table: dict[str, dict[str, str]]
#   = json.load(open(os.path.join(os.path.dirname(__file__), 'table.json')))
cml_table: dict[str, dict[str, str]] = json.load(
    open(os.path.join(os.path.dirname(__file__), "table.json"))
)

cml_rules: list[Rule] = [
    # type keyworkds
    Rule(name="i8", pattern=r"i8", alias="type"),
    Rule(name="i16", pattern=r"i16", alias="type"),
    Rule(name="i32", pattern=r"i32", alias="type"),
    Rule(name="i64", pattern=r"i64", alias="type"),
    Rule(name="ui8", pattern=r"ui8", alias="type"),
    Rule(name="ui16", pattern=r"ui16", alias="type"),
    Rule(name="ui32", pattern=r"ui32", alias="type"),
    Rule(name="ui64", pattern=r"ui64", alias="type"),
    Rule(name="f32", pattern=r"f32", alias="type"),
    Rule(name="f64", pattern=r"f64", alias="type"),
    Rule(name="bool", pattern=r"bool", alias="type"),
    # flow control keyworkds
    Rule(name="if", pattern=r"if"),
    Rule(name="else", pattern=r"else"),
    # Rule(name='elif', pattern=r'elif'),
    Rule(name="while", pattern=r"while"),
    Rule(name="for", pattern=r"for"),
    # IO
    Rule(name="read", pattern=r"read"),
    Rule(name="write", pattern=r"write"),
    # literals
    Rule(name="comment", pattern=r"#[^\n]*"),
    Rule(name="literal_float", pattern=r"\-?[0-9]*\.[0-9]+"),
    Rule(name="literal_hex", pattern=r"0x[0-9a-f]+", alias="literal_int"),
    Rule(name="literal_bin", pattern=r"0b[0-1]+", alias="literal_int"),
    Rule(name="literal_oct", pattern=r"0o[0-7]+", alias="literal_int"),
    Rule(name="literal_int", pattern=r"\-?[0-9]+"),
    Rule(name="literal_true", pattern=r"true", alias="literal_bool"),
    Rule(name="literal_false", pattern=r"false", alias="literal_bool"),
    Rule(name="literal_str", pattern=r'\"[^\"\n]*"', alias="literal_str"),
    # scopes
    Rule(name="left_parenthesis", pattern=r"\(", alias="("),
    Rule(name="right_parenthesis", pattern=r"\)", alias=")"),
    Rule(name="left_braces", pattern=r"\{", alias="{"),
    Rule(name="right_braces", pattern=r"\}", alias="}"),
    # Rule(name='left_brackets',     pattern=r'\[', alias='['),
    # Rule(name='right_brackets',    pattern=r'\]', alias=']'),
    # Sequence
    Rule(name="comma", pattern=r"\,", alias=","),
    Rule(name="end", pattern=r"\;", alias=";"),
    # Operations - Relational
    Rule(name="equals", pattern=r"\=\=", alias="rel_op"),
    Rule(name="not_equals", pattern=r"\!\=", alias="rel_op"),
    Rule(name="less_equal", pattern=r"\<\=", alias="rel_op"),
    Rule(name="more_equal", pattern=r"\>\=", alias="rel_op"),
    Rule(name="less_than", pattern=r"\<", alias="rel_op"),
    Rule(name="more_than", pattern=r"\>", alias="rel_op"),
    # Operations - Logical
    Rule(name="or", pattern=r"or", alias="bool_op"),
    Rule(name="and", pattern=r"and", alias="bool_op"),
    Rule(name="not", pattern=r"not"),
    # Operations - inplace
    # Rule(name='increment',  pattern=r'\+\+', alias='op_inc'),
    # Rule(name='decrement',  pattern=r'\-\-', alias='op_inc'),
    # Attributions
    Rule(name="attrib", pattern=r"\="),
    # Attributions - arithmetic
    Rule(name="a_sum", pattern=r"\+\=", alias="attrib_op"),
    Rule(name="a_sub", pattern=r"\-\=", alias="attrib_op"),
    Rule(name="a_mul", pattern=r"\*\=", alias="attrib_op"),
    Rule(name="a_div", pattern=r"\/\=", alias="attrib_op"),
    Rule(name="a_mod", pattern=r"\%\=", alias="attrib_op"),
    # Operations - arithmetic
    Rule(name="sum", pattern=r"\+", alias="arith_op_sum"),
    Rule(name="sub", pattern=r"\-", alias="arith_op_sum"),
    Rule(name="mul", pattern=r"\*", alias="arith_op_mul"),
    Rule(name="div", pattern=r"\/", alias="arith_op_mul"),
    Rule(name="mod", pattern=r"\%", alias="arith_op_mul"),
    # White space
    Rule(name="newline", pattern=r"\n"),
    Rule(name="space", pattern=r" ", alias="ws"),
    Rule(name="tab", pattern=r"\t", alias="ws"),
    # Identifiers
    Rule(name="id", pattern=r"[a-zA-Z_]\w*"),
    # Missmatch
    Rule(name="missmatch", pattern=r".", alias="unknown"),
]
