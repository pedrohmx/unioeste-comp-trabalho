# cml ruleset

from dataclasses import dataclass

@dataclass
class Rule:
    name:    str
    pattern: str
    alias:   str | None = None

cml_rules = [
    # type keyworkds
    Rule(name='i8',   pattern=r'i8',   alias='type'),
    Rule(name='i16',  pattern=r'i16',  alias='type'),
    Rule(name='i32',  pattern=r'i32',  alias='type'),
    Rule(name='i64',  pattern=r'i64',  alias='type'),
    Rule(name='ui8',  pattern=r'ui8',  alias='type'),
    Rule(name='ui16', pattern=r'ui16', alias='type'),
    Rule(name='ui32', pattern=r'ui32', alias='type'),
    Rule(name='ui64', pattern=r'ui64', alias='type'),
    Rule(name='f32',  pattern=r'f32',  alias='type'),
    Rule(name='f64',  pattern=r'f64',  alias='type'),
    Rule(name='bool', pattern=r'bool', alias='type'),
    
    # flow control keyworkds
    Rule(name='if', pattern=r'if'),
    Rule(name='else', pattern=r'else'),
    Rule(name='elif', pattern=r'elif'),
    Rule(name='while', pattern=r'while'),
    Rule(name='for', pattern=r'for'),
    
    # IO
    Rule(name='read', pattern=r'read'),
    Rule(name='write', pattern=r'write'),

    # literals
    Rule(name='comment',       pattern=r'#[^\n]*'),
    Rule(name='literal_float', pattern=r'\-?[0-9]*\.[0-9]+'),
    Rule(name='literal_int',   pattern=r'\-?[0-9]+'),
    Rule(name='literal_hex',   pattern=r'0x[0-9a-f]+', alias='literal_int'),
    Rule(name='literal_bin',   pattern=r'0b[0-1]+',    alias='literal_int'),
    Rule(name='literal_oct',   pattern=r'0o[0-7]+',    alias='literal_int'),
    Rule(name='literal_str',   pattern=r'\"[^\"\n]*"', alias='literal_string'),
    
    # scopes
    Rule(name='left_parenthesis',  pattern=r'\(', alias='('),
    Rule(name='right_parenthesis', pattern=r'\)', alias=')'),
    Rule(name='left_braces',       pattern=r'\{', alias='{'),
    Rule(name='right_braces',      pattern=r'\}', alias='}'),
    # Rule(name='left_brackets',     pattern=r'\[', alias='['),
    # Rule(name='right_brackets',    pattern=r'\]', alias=']'),
    
    # Sequence
    Rule(name='comma', pattern=r'\,', alias=','),
    Rule(name='end',   pattern=r'\;', alias=';'),

    # Operations - logical
    Rule(name='equals',     pattern=r'\=\=', alias='op'),
    Rule(name='not_equals', pattern=r'\!\=', alias='op'),
    Rule(name='less_equal', pattern=r'\<\=', alias='op'),
    Rule(name='more_equal', pattern=r'\>\=', alias='op'),
    Rule(name='or',         pattern=r'\|\|', alias='op'),
    Rule(name='and',        pattern=r'\&\&', alias='op'),
    Rule(name='less_than',  pattern=r'\<',   alias='op'),
    Rule(name='more_than',  pattern=r'\>',   alias='op'),
    
    # Operations - inplace
    Rule(name='increment',  pattern=r'\+\+', alias='op'),
    Rule(name='decrement',  pattern=r'\-\-', alias='op'),

    # Attributions
    Rule(name='attrib', pattern=r'\=',  alias='op'),
    # Attributions - arithmetic
    Rule(name='a_sum', pattern=r'\+\=', alias='op'),
    Rule(name='a_sub', pattern=r'\-\=', alias='op'),
    Rule(name='a_mul', pattern=r'\*\=', alias='op'),
    Rule(name='a_div', pattern=r'\/\=', alias='op'),
    Rule(name='a_mod', pattern=r'\%\=', alias='op'),

    # Operations - arithmetic
    Rule(name='sum', pattern=r'\+', alias='op'),
    Rule(name='sub', pattern=r'\-', alias='op'),
    Rule(name='mul', pattern=r'\*', alias='op'),
    Rule(name='div', pattern=r'\/', alias='op'),
    Rule(name='mod', pattern=r'\%', alias='op'),

    # White space
    Rule(name='newline', pattern=r'\n'),
    Rule(name='space',   pattern=r' ',  alias='ws'),
    Rule(name='tab',     pattern=r'\t', alias='ws'),

    # Identifiers
    Rule(name='id', pattern=r'[a-zA-Z_]\w*'),

    # Missmatch
    Rule(name='missmatch', pattern=r'.', alias='unknown'),

    # Rule(name='', pattern=r''),
    # Rule(name='', pattern=r'', alias=''),
]
