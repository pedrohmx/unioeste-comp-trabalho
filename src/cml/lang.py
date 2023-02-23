from .util import Rule

cml_res: list[Rule] = [
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
    # Rule(name='elif', pattern=r'elif'),
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
    Rule(name='literal_true',  pattern=r'true', alias='literal_bool'),
    Rule(name='literal_false', pattern=r'false', alias='literal_bool'),

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

    # Operations - Relational
    Rule(name='equals',     pattern=r'\=\=', alias='rel_op'),
    Rule(name='not_equals', pattern=r'\!\=', alias='rel_op'),
    Rule(name='less_equal', pattern=r'\<\=', alias='rel_op'),
    Rule(name='more_equal', pattern=r'\>\=', alias='rel_op'),
    Rule(name='less_than',  pattern=r'\<',   alias='rel_op'),
    Rule(name='more_than',  pattern=r'\>',   alias='rel_op'),

    # Operations - Logical
    Rule(name='or',         pattern=r'or',  alias='bool_op'),
    Rule(name='and',        pattern=r'and', alias='bool_op'),
    Rule(name='not',        pattern=r'not'),

    # Operations - inplace
    # Rule(name='increment',  pattern=r'\+\+', alias='op_inc'),
    # Rule(name='decrement',  pattern=r'\-\-', alias='op_inc'),

    # Attributions
    Rule(name='attrib', pattern=r'\='),
    # Attributions - arithmetic
    Rule(name='a_sum', pattern=r'\+\=', alias='attrib_op'),
    Rule(name='a_sub', pattern=r'\-\=', alias='attrib_op'),
    Rule(name='a_mul', pattern=r'\*\=', alias='attrib_op'),
    Rule(name='a_div', pattern=r'\/\=', alias='attrib_op'),
    Rule(name='a_mod', pattern=r'\%\=', alias='attrib_op'),

    # Operations - arithmetic
    Rule(name='sum', pattern=r'\+', alias='arith_op_sum'),
    Rule(name='sub', pattern=r'\-', alias='arith_op_sum'),
    Rule(name='mul', pattern=r'\*', alias='arith_op_mul'),
    Rule(name='div', pattern=r'\/', alias='arith_op_mul'),
    Rule(name='mod', pattern=r'\%', alias='arith_op_mul'),

    # White space
    Rule(name='newline', pattern=r'\n'),
    Rule(name='space',   pattern=r' ',  alias='ws'),
    Rule(name='tab',     pattern=r'\t', alias='ws'),

    # Identifiers
    Rule(name='id', pattern=r'[a-zA-Z_]\w*'),

    # Missmatch
    Rule(name='missmatch', pattern=r'.', alias='unknown'),
]

grammar_dev = [
    {
        'nonterm': "PROG'",
        'dev': ['PROG']},
    {
        'nonterm': 'PROG',
        'dev': ['STMTS']},
    {
        'nonterm': 'STMTS',
        'dev': []},
    {
        'nonterm': 'STMTS',
        'dev': ['STMTS STMT']},
    {
        'nonterm': 'STMT',
        'dev': ['FLOW']},
    {
        'nonterm': 'STMT',
        'dev': ['DECL_STMT ;']},
    {
        'nonterm': 'STMT',
        'dev': ['COMMAND ;']},
    {
        'nonterm': 'STMT',
        'dev': ['ATTRIB_STMT ;']},
    {
        'nonterm': 'DECL_STMT',
        'dev': ['type id DECL_END']},
    {
        'nonterm': 'DECL_END',
        'dev': ['attrib EXPR']},
    {
        'nonterm': 'DECL_END',
        'dev': []},
    {
        'nonterm': 'ATTRIB_STMT',
        'dev': ['id ATTRIB_END']},
    {
        'nonterm': 'ATTRIB_END',
        'dev': ['attrib EXPR']},
    {
        'nonterm': 'ATTRIB_END',
        'dev': ['attrib_op EXPR']},
    {
        'nonterm': 'EXPR',
        'dev': ['ARITH_EXPR']},
    {
        'nonterm': 'EXPR',
        'dev': ['BOOL_EXPR']},
    {
        'nonterm': 'BOOL_EXPR',
        'dev': ['VAR bool_op VAR']},
    {
        'nonterm': 'BOOL_EXPR',
        'dev': ['REL_EXPR']},
    {
        'nonterm': 'BOOL_EXPR',
        'dev': ['not VAR']},
    {
        'nonterm': 'ARITH_EXPR',
        'dev': ['VAR arith_op_sum VAR']},
    {
        'nonterm': 'ARITH_EXPR',
        'dev': ['VAR arith_op_mul VAR']},
    {
        'nonterm': 'REL_EXPR',
        'dev': ['VAR rel_op VAR']},
    {
        'nonterm': 'FLOW',
        'dev': ['IF_STMT']},
    {
        'nonterm': 'FLOW',
        'dev': ['FOR_STMT']},
    {
        'nonterm': 'FLOW',
        'dev': ['WHILE_STMT']},
    {
        'nonterm': 'IF_STMT',
        'dev': ['if ( BOOL_EXPR ) { STMTS } ELSE_STMT']},
    {
        'nonterm': 'ELSE_STMT',
        'dev': []},
    {
        'nonterm': 'ELSE_STMT',
        'dev': ['else { STMTS }']},
    {
        'nonterm': 'WHILE_STMT',
        'dev': ['while ( BOOL_EXPR ) { STMTS }']},
    {
        'nonterm': 'FOR_STMT',
        'dev': ['for ( DECL_STMT ; BOOL_EXPR ; ATTRIB_STMT ) { STMTS }']},
    {
        'nonterm': 'COMMAND',
        'dev': ['read id']},
    {
        'nonterm': 'COMMAND',
        'dev': ['write VAR WCHAIN']},
    {
        'nonterm': 'WCHAIN',
        'dev': []},
    {
        'nonterm': 'WCHAIN',
        'dev': [', VAR WCHAIN']},
    {
        'nonterm': 'VAR',
        'dev': ['id']},
    {
        'nonterm': 'VAR',
        'dev': ['LITERAL']},
    {
        'nonterm': 'LITERAL',
        'dev': ['literal_bool']},
    {
        'nonterm': 'LITERAL',
        'dev': ['literal_float']},
    {
        'nonterm': 'LITERAL',
        'dev': ['literal_str']},
    {
        'nonterm': 'LITERAL',
        'dev': ['literal_int']},
]

slr_table: dict[str, list[str|int]] = {
    "for": [
        "r2","s3","e","e","e","r23","r3","e","e","r4","e","e","r22","r24","e","e","e","e","e","e","e","r6","e","e","e","e","r5","e","e","e","e","e","e","e","r7","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","r2","e","e","e","r2","e","s3","s3","e","r28","r26","e","e","r25","r2","r2","s3","s3","r29","r27"
    ],
    "read": [
        "r2","s4","e","e","e","r23","r3","e","e","r4","e","e","r22","r24","e","e","e","e","e","e","e","r6","e","e","e","e","r5","e","e","e","e","e","e","e","r7","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","r2","e","e","e","r2","e","s4","s4","e","r28","r26","e","e","r25","r2","r2","s4","s4","r29","r27"
    ],
    "rel_op": [
        "e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","r37","r38","e","r36","r34","r35","r39","e","e","e","e","e","s53","e","e","e","e","s53","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e"
    ],
    "literal_float": [
        "e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","s27","e","e","e","e","e","e","s27","s27","s27","e","e","e","e","e","e","e","e","e","e","s27","e","s27","e","e","e","s27","e","e","e","e","e","e","e","s27","e","s27","e","s27","s27","e","e","s27","s27","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e"
    ],
    "}": [
        "r2","e","e","e","e","r23","r3","e","e","r4","e","e","r22","r24","e","e","e","e","e","e","e","r6","e","e","e","e","r5","e","e","e","e","e","e","e","r7","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","r2","e","e","e","r2","e","s73","s74","e","r28","r26","e","e","r25","r2","r2","s82","s83","r29","r27"
    ],
    "(": [
        "e","e","e","s18","e","e","e","e","e","e","s22","e","e","e","e","e","e","s35","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e"
    ],
    "literal_str": [
        "e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","s28","e","e","e","e","e","e","s28","s28","s28","e","e","e","e","e","e","e","e","e","e","s28","e","s28","e","e","e","s28","e","e","e","e","e","e","e","s28","e","s28","e","s28","s28","e","e","s28","s28","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e"
    ],
    "attrib": [
        "e","e","e","e","e","e","e","e","e","e","e","s23","e","e","e","e","e","e","e","e","s37","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e"
    ],
    "else": [
        "e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","s76","e","e","e","e","e","e","e","e","e"
    ],
    "type": [
        "r2","s7","e","e","e","r23","r3","e","e","r4","e","e","r22","r24","e","e","e","e","s7","e","e","r6","e","e","e","e","r5","e","e","e","e","e","e","e","r7","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","r2","e","e","e","r2","e","s7","s7","e","r28","r26","e","e","r25","r2","r2","s7","s7","r29","r27"
    ],
    "not": [
        "e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","s41","s41","s41","e","e","e","e","e","e","e","e","e","e","s41","e","s41","e","e","e","e","e","e","e","e","e","e","e","e","e","s41","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e"
    ],
    ";": [
        "e","e","e","e","e","e","e","e","s21","e","e","e","e","e","s26","e","s34","e","e","r30","r10","e","e","e","e","r11","e","r37","r38","r32","r36","r34","r35","r39","e","e","s51","e","r8","e","r17","e","e","r14","e","r15","r12","r13","r31","e","e","e","r9","e","e","r18","e","e","e","r32","e","s69","r21","r16","e","r20","r19","r33","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e"
    ],
    "while": [
        "r2","s10","e","e","e","r23","r3","e","e","r4","e","e","r22","r24","e","e","e","e","e","e","e","r6","e","e","e","e","r5","e","e","e","e","e","e","e","r7","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","r2","e","e","e","r2","e","s10","s10","e","r28","r26","e","e","r25","r2","r2","s10","s10","r29","r27"
    ],
    "arith_op_mul": [
        "e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","r37","r38","e","r36","r34","r35","r39","e","e","e","e","e","e","e","e","e","e","s57","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e"
    ],
    "literal_bool": [
        "e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","s30","e","e","e","e","e","e","s30","s30","s30","e","e","e","e","e","e","e","e","e","e","s30","e","s30","e","e","e","s30","e","e","e","e","e","e","e","s30","e","s30","e","s30","s30","e","e","s30","s30","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e"
    ],
    "id": [
        "r2","s11","e","e","s19","r23","r3","s20","e","r4","e","e","r22","r24","e","s31","e","e","e","e","e","r6","s31","s31","s31","e","r5","e","e","e","e","e","e","e","r7","s31","e","s31","e","e","e","s31","e","e","e","e","e","e","e","s31","e","s31","e","s31","s31","e","e","s31","s31","e","e","e","e","e","r2","e","e","e","r2","s11","s11","s11","e","r28","r26","e","e","r25","r2","r2","s11","s11","r29","r27"
    ],
    "attrib_op": [
        "e","e","e","e","e","e","e","e","e","e","e","s24","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e"
    ],
    "{": [
        "e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","s64","e","e","e","s68","e","e","e","e","e","e","e","e","e","e","e","e","e","e","s78","s79","e","e","e","e","e","e","e"
    ],
    "literal_int": [
        "e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","s33","e","e","e","e","e","e","s33","s33","s33","e","e","e","e","e","e","e","e","e","e","s33","e","s33","e","e","e","s33","e","e","e","e","e","e","e","s33","e","s33","e","s33","s33","e","e","s33","s33","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e"
    ],
    "bool_op": [
        "e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","r37","r38","e","r36","r34","r35","r39","e","e","e","e","e","s54","e","e","e","e","s54","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e"
    ],
    "arith_op_sum": [
        "e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","r37","r38","e","r36","r34","r35","r39","e","e","e","e","e","e","e","e","e","e","s58","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e"
    ],
    "write": [
        "r2","s15","e","e","e","r23","r3","e","e","r4","e","e","r22","r24","e","e","e","e","e","e","e","r6","e","e","e","e","r5","e","e","e","e","e","e","e","r7","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","r2","e","e","e","r2","e","s15","s15","e","r28","r26","e","e","r25","r2","r2","s15","s15","r29","r27"
    ],
    ")": [
        "e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","r11","e","r37","r38","e","r36","r34","r35","r39","e","e","e","e","e","e","r17","e","s56","r14","e","r15","r12","r13","e","e","s60","e","e","e","e","r18","e","e","e","e","e","e","r21","r16","e","r20","r19","e","e","e","e","e","s75","e","e","e","e","e","e","e","e","e","e","e"
    ],
    ",": [
        "e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","r37","r38","s49","r36","r34","r35","r39","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","s49","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e"
    ],
    "if": [
        "r2","s17","e","e","e","r23","r3","e","e","r4","e","e","r22","r24","e","e","e","e","e","e","e","r6","e","e","e","e","r5","e","e","e","e","e","e","e","r7","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","r2","e","e","e","r2","e","s17","s17","e","r28","r26","e","e","r25","r2","r2","s17","s17","r29","r27"
    ],
    "$": [
        "r2","r1","acc","e","e","r23","r3","e","e","r4","e","e","r22","r24","e","e","e","e","e","e","e","r6","e","e","e","e","r5","e","e","e","e","e","e","e","r7","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","r2","e","e","e","r2","e","e","e","e","r28","r26","e","e","r25","r2","r2","e","e","r29","r27"
    ],
    "COMMAND": [
        "e",8,"e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e",8,8,"e","e","e","e","e","e","e","e",8,8,"e","e"
    ],
    "FLOW": [
        "e",9,"e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e",9,9,"e","e","e","e","e","e","e","e",9,9,"e","e"
    ],
    "STMTS": [
        1,"e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e",70,"e","e","e",71,"e","e","e","e","e","e","e","e","e",80,81,"e","e","e","e"
    ],
    "PROG": [
        2,"e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e"
    ],
    "WCHAIN": [
        "e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e",48,"e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e",67,"e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e"
    ],
    "DECL_END": [
        "e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e",38,"e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e"
    ],
    "FOR_STMT": [
        "e",5,"e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e",5,5,"e","e","e","e","e","e","e","e",5,5,"e","e"
    ],
    "IF_STMT": [
        "e",12,"e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e",12,12,"e","e","e","e","e","e","e","e",12,12,"e","e"
    ],
    "LITERAL": [
        "e","e","e","e","e","e","e","e","e","e","e","e","e","e","e",32,"e","e","e","e","e","e",32,32,32,"e","e","e","e","e","e","e","e","e","e",32,"e",32,"e","e","e",32,"e","e","e","e","e","e","e",32,"e",32,"e",32,32,"e","e",32,32,"e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e"
    ],
    "ARITH_EXPR": [
        "e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e",43,43,"e","e","e","e","e","e","e","e","e","e","e","e",43,"e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e"
    ],
    "WHILE_STMT": [
        "e",13,"e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e",13,13,"e","e","e","e","e","e","e","e",13,13,"e","e"
    ],
    "ATTRIB_END": [
        "e","e","e","e","e","e","e","e","e","e","e",25,"e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e"
    ],
    "DECL_STMT": [
        "e",14,"e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e",36,"e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e",14,14,"e","e","e","e","e","e","e","e",14,14,"e","e"
    ],
    "VAR": [
        "e","e","e","e","e","e","e","e","e","e","e","e","e","e","e",29,"e","e","e","e","e","e",39,44,44,"e","e","e","e","e","e","e","e","e","e",39,"e",44,"e","e","e",55,"e","e","e","e","e","e","e",59,"e",39,"e",62,63,"e","e",65,66,"e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e"
    ],
    "BOOL_EXPR": [
        "e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e",42,45,45,"e","e","e","e","e","e","e","e","e","e",50,"e",45,"e","e","e","e","e","e","e","e","e","e","e","e","e",61,"e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e"
    ],
    "ATTRIB_STMT": [
        "e",16,"e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e",72,16,16,"e","e","e","e","e","e","e","e",16,16,"e","e"
    ],
    "EXPR": [
        "e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e",46,47,"e","e","e","e","e","e","e","e","e","e","e","e",52,"e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e"
    ],
    "ELSE_STMT": [
        "e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e",77,"e","e","e","e","e","e","e","e","e"
    ],
    "REL_EXPR": [
        "e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e",40,40,40,"e","e","e","e","e","e","e","e","e","e",40,"e",40,"e","e","e","e","e","e","e","e","e","e","e","e","e",40,"e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e"
    ],
    "STMT": [
        "e",6,"e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e","e",6,6,"e","e","e","e","e","e","e","e",6,6,"e","e"
    ]
}


# grammar: dict[
#     str,
#     str | list[str] | dict[
#         str,
#         list[
#             list[str] |
#             None]
#     ]
# ] = {
#     "starter": "program",
#     "prod": {},
#     "term": [
#         'id', 'type', 'attrib',
#         'read', 'write', 'if', 'else', 'for', 'while', 'not',
#         'arith_op_sum', 'arith_op_mul', 'bool_op', 'rel_op', 'attrib_op',
#         ';', ',', '(', ')', '{', '}',
#         'literal_int', 'literal_float', 'literal_string', 'literal_bool',
#     ],
#     "nterm": [
#         "program", "stmts", "stmt"
#     ],
# }

# v3 = {}