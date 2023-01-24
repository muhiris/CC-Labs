import ply.lex as lex

inputIs = open('input.txt', 'r')
tokenized = []
asNum = []
tokens = (
    'INTEGER',
    'FLOAT',
    'PLUS',
    'MINUS',
    'TIMES',
    'LPAREN',
    'RPAREN',
    'EQUAL',
    'NAME'
)
t_PLUS = r'\+'
t_MINUS = r'\-'
t_TIMES = r'\*'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_EQUAL = r'\='
t_NAME = r'[a-zA-Z_][a-zA-Z0-9_]*'

def t_FLOAT(t):
    r'-?\d+\.\d+|\d+\.\d+e-?\d+'
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
    tokenized.append(str(tok.value))
print(tokenized)
for index, x in enumerate(tokenized):
    for ind, i in enumerate(x):
        if (i == ','):
            print(x[0:1])
            print(x[1:])
            tokenized[index] = x[0:1]
            tokenized[index + 1] = x[1:]
print(tokenized)


def isfloat(num):
    try:
        float(num)
        return True
    except ValueError:
        return False
print("verfied")
idARRAY = []
for index, x in enumerate(tokenized):
    if (x.isalpha() and x != 'int'):
        idARRAY.append('i')
    elif (x.isdigit()):
        idARRAY.append('r')
    else:
        if (not isfloat(x)):
            idARRAY.append(x)
# printing accepted array
print(idARRAY)
with open('table.txt' ,'r') as obj:
    tableIs = [[y.replace('Â\xa0','') for y in x.split(',')] for x in obj.read().split('\n') if x!= ''  ]
print('Table is:')
for row in tableIs:
    print(row)

table = {}
terminals =['=' ,'-' ,'+' ,'(' ,')' ,'r' ,'i' ,'$']  #lets take r for digits and i for indexes
non_terminals =['S' ,'E' ,'T' ,'F','V']

for index , value in enumerate(tableIs):
    table[index] ={}
    for ind, val in enumerate(terminals + non_terminals):
        table[index][val] = value[ind]
print("Table Dictionary")
for key , value in table.items():
    print(key , value)


input  = idARRAY + ['$']
production =[ "S->V=E","E->E-T","E->T","T->T+F","T->F","T->(E)","F->r","V->i"]
sementics = ["S.val = E.val; V.val = E.val; print(S.val)" ,"E.val = E1.val - T.val" ,"E.val = T.val" ,"T.val = T.val + F.val" ,"T.val = F.val" ,"F.val = E.val" ,"F.val = digit.lexval" ,"V.val =id.lexval"]



stack = [0]
index= 0
bool = True
print('Stack    Input    Action    Rule')
while bool:
    data = [str(stack), " ".join(input)]
    if (stack[-1] == '' ):
        print("*////////Error\\\\\\\\* ====  ", end="")
        print('got null value  unParsable')

        break

    Top_Stack = int(stack[-1])
    Curr_input = input[index]

    # if table is correct, element is production number Rx Sx or accept
    try:
        element = table[Top_Stack][Curr_input]
    except:
        print("Wrong table. Error do not pass")

    if (element == 'acc'):
        print("Boom! accepted")
        break

    if (element[0] == 's' or element[0] == 'S'):
        stack.append(Curr_input)
        temp = ""
        for x in range(1, len(element)):
            temp += element[x]
            print(temp)
        stack.append(temp)
        index += 1

        data.append(element)
        print(data[0] + " " + data[1] + " " + data[2])
    elif (element[0] == 'r' or element[0] == 'R'):
        ruleNo = production[int(element[1])]
        # each production has 3 characters of terminal symbol so subtracting 3 i.e. for 'X' '-' '>' it is 3
        extraLen = 3
        prodleng = len(ruleNo) - extraLen

        for i in range(prodleng * 2):
            try:
                stack.pop()
            except:
                print("There is error more pops then expected")
                bool = False
                break
            if (bool == False):
                break
        #   appending terminal symbol you reduced with
        stack.append(ruleNo[0])

        appendedTerminal = (stack[-1])
        previousToTerminal = int(stack[-2])
        #   adding that goto value
        stack.append(table[previousToTerminal][appendedTerminal])
        data.append(table[previousToTerminal][appendedTerminal])
        data.append(sementics[int(element[1])])
        print(data[0] + " " + data[1] + " " + data[2] + " " + data[3])


