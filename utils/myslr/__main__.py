import argparse
import json
# from pprint import pprint
from slr_parser.grammar import Grammar
from slr_parser.slr_parser import SLRParser
# from .grammar import Grammar
# from .slr import SLRParser

aparser = argparse.ArgumentParser()
aparser.add_argument('grammar', type=argparse.FileType('r'), help='text file to be used as grammar')

args = aparser.parse_args()

slr = SLRParser(Grammar(args.grammar.read()))
table = slr.construct_table()

grammar = []
for head, body in slr.G_indexed:
    grammar.append({
        'head': head,
        'body': body
    })

for state in table.keys():
    for key in table[state].keys():
        if table[state][key] == "":
            table[state][key] = "e"
        else:
            table[state][key] = str(table[state][key])

with open("table.json", "w") as f:
    print(json.dumps(table), file=f)

with open("grammar.json", "w") as f:
    print(json.dumps(grammar), file=f)

# slr.print_info()
