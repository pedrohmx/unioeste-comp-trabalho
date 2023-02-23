v2 = {
    'program': [['stmts']],
    'stmts': [
        ['stmts', 'stmt'],
        None
    ],
    'stmt': [['decl_stmt'], ['attrib_stmt'], ['command']],
    'decl_stmt': [['type', 'id', 'decl_end']],
    'decl_end': [
        ['attrib', 'expr'],
        None
    ],
    'attrib_stmt': [['var', 'attrib_end', ';']],
    'attrib_end': [
        ['attrib', 'expr'],
        ['attrib_op', 'expr']
    ],
    'expr': [
        ['arith_expr'],
        ['bool_expr'],
        ['rel_expr']
    ],
    'rel_expr': [['arith_expr', 'rel_op', 'arith_expr']],
    'arith_expr': [
        ['arith_expr', 'arith_op_sum', 'arith_term'],
        ['arith_term']
    ],
    'arith_term': [
        ['arith_term', 'arith_op_mul', 'arith_term'],
        ["(", 'arith_expr', ")"],
        ['var'],
        ['literal']
    ],
    'bool_expr': [
        ['not', 'bool_expr'],
        ['boolean', 'bool_expr_chain']
    ],
    'bool_expr_chain': [
        ['bool_op', 'boolean'],
        None
    ],
    'boolean': [
        ['rel_expr'],['literal_bool'], ['var']
    ],
    'command': [
        ['read', 'var', ';'],
        ['write', 'writables', ';'],
        ['if_stmt'],
        ['while_stmt'],
        ['for_stmt']
    ],
    'writables': [['writable', 'writable_chain']],
    'writable_chain': [[',', 'writable', 'writable_chain'], None],
    'writable': [['literal'], ['var'], ['expr']],
    'literal': [['literal_int'], ['literal_float'], ['literal_bool'], ['literal_str']],
    'var': [['id']],
    'if_stmt': [['if', '(', 'bool_expr', ')', '{', 'stmts', '}', 'else_stmt']],
    'else_stmt': [['else', '{', 'stmts', '}'], None],
    'while_stmt': [['while', '(', 'bool_expr', ')', '{', 'stmts', '}']],
    'for_stmt': [['for', '(', 'decl', ';', 'bool_expr', ';', 'attrib'')', '{', 'stmts', '}']],

}

v3 = [
    {
        'nterm': 'PROG',
        'prod': ['STMTS']
    },{
        'nterm': 'STMTS',
        'prod': ['STMTS' 'STMT']
    },{
        'nterm': 'STMTS',
        'prod': ['']
    },{
        'nterm': 'STMT',
        'prod': ['DECL_STMT' ';']
    },{
        'nterm': 'STMT',
        'prod': ['ATTRIB_STMT' ';']
    },{
        'nterm': 'STMT',
        'prod': ['COMMAND' ';']
    },{
        'nterm': 'STMT',
        'prod': ['FLOW']
    },{
        'nterm': 'DECL_STMT',
        'prod': ['type' 'id' 'DECL_END']
    },{
        'nterm': 'DECL_END',
        'prod': ['attrib' 'EXPR']
    },{
        'nterm': 'DECL_END',
        'prod': ['']
    },{
        'nterm': 'ATTRIB_STMT',
        'prod': ['id' 'ATTRIB_END']
    },{
        'nterm': 'ATTRIB_END',
        'prod': ['ATTRIB' 'EXPR']
    },{
        'nterm': 'ATTRIB_END',
        'prod': ['ATTRIB_OP' 'EXPR']
    },{
        'nterm': 'EXPR',
        'prod': ['BOOL_EXPR']
    },{
        'nterm': 'EXPR',
        'prod': ['ARITH_EXPR']
    },{
        'nterm': 'BOOL_EXPR',
        'prod': ['VAR' 'BOOL_OP' 'VAR']
    },{
        'nterm': 'BOOL_EXPR',
        'prod': ['not' 'VAR']
    },{
        'nterm': 'BOOL_EXPR',
        'prod': ['REL_EXPR']
    },{
        'nterm': 'ARITH_EXPR',
        'prod': ['VAR' 'ARITH_OP_SUM' 'VAR']
    },{
        'nterm': 'ARITH_EXPR',
        'prod': ['VAR' 'ARITH_OP_MUL' 'VAR']
    },{
        'nterm': 'REL_EXPR',
        'prod': ['VAR' 'REL_OP' 'VAR']
    },{
        'nterm': 'FLOW',
        'prod': ['IF_STMT']
    },{
        'nterm': 'FLOW',
        'prod': ['WHILE_STMT']
    },{
        'nterm': 'FLOW',
        'prod': ['FOR_STMT']
    },{
        'nterm': 'IF_STMT',
        'prod': ['if' '(' 'BOOL_EXPR' ')' '{' 'STMTS' '}' 'ELSE_STMT']
    },{
        'nterm': 'ELSE_STMT',
        'prod': ['else' '{' 'STMTS' '}']
    },{
        'nterm': 'ELSE_STMT',
        'prod': ['']
    },{
        'nterm': 'WHILE_STMT',
        'prod': ['while' '(' 'BOOL_EXPR' ')' '{' 'STMTS' '}']
    },{
        'nterm': 'FOR_STMT',
        'prod': ['for' '(' 'DECL_STMT' ';' 'BOOL_EXPR' ';' 'ATTRIB' ')' '{' 'STMTS' '}']
    },{
        'nterm': 'COMMAND',
        'prod': ['read' 'id']
    },{
        'nterm': 'COMMAND',
        'prod': ['write' 'VAR' 'WCHAIN']
    },{
        'nterm': 'WCHAIN',
        'prod': [',' 'VAR' 'WCHAIN']
    },{
        'nterm': 'WCHAIN',
        'prod': ['']
    },{
        'nterm': 'VAR',
        'prod': ['id']
    },{
        'nterm': 'VAR',
        'prod': ['LITERAL']
    },{
        'nterm': 'LITERAL',
        'prod': ["literal_int"]
    },{
        'nterm': 'LITERAL',
        'prod': ["literal_float"]
    },{
        'nterm': 'LITERAL',
        'prod': ["literal_bool"]
    },{
        'nterm': 'LITERAL',
        'prod': ["literal_str"]
    },
]