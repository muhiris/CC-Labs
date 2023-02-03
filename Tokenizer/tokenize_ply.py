import ply.lex as lex

inputIs = open('tokens.txt', 'r')
tokenized = []
asNum = []
tokens = (
    'INTEGER',
    'FLOAT',
    'PLUS',
    'TIMES',
    'LPAREN',
    'RPAREN',
    'EQUAL',
    'NAME'
)
t_PLUS = r'\+'
t_TIMES = r'\*'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_EQUAL = r'\='
t_NAME = r'[a-zA-Z_][a-zA-Z0-9_]*'

def t_FLOAT(t):
    r'[+-]?([0-9]*[.])?[0-9]+'
    t.value = float(t.value)
    return t

def t_INTEGER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)
t_ignore = ' \t'
def t_error(t):
    t.lexer.skip(1)
lexer = lex.lex()
data = inputIs.read()
lexer.input(data)

while True:
    tok = lexer.token()
    if not tok:
        break
    tokenized.append(tok.value)
print(tokenized)

