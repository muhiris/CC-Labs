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
    if tok.value == 'hate' or tok.value=='like'or tok.value=='a' or tok.value=='tea' or tok.value=='prefer' or tok.value=='morning' or tok.value=='flight' or tok.value=='i':
        tokenized.append(str(tok.value))
print("Tokenized is:", tokenized)


idARRAY = []
for i in tokenized:
    idARRAY.append(i[0])
print('After converting to id way',idARRAY)
with open('table.txt' ,'r') as obj:
    tableIs = [[y.replace('Â\xa0','') for y in x.split(',')] for x in obj.read().split('\n') if x!= ''  ]
#print('Table is:')
#for row in tableIs:
#    print(row)

table = {}
terminals =['i' ,'m' ,'f' ,'t' ,'a' ,'p' ,'l','h' ,'$']  #lets take r for digits and i for indexes
non_terminals =['S' ,'N','P','V','M','O','D','Q']

for index , value in enumerate(tableIs):
    table[index] ={}
    for ind, val in enumerate(terminals + non_terminals):
        table[index][val] = value[ind]
print("Table Dictionary")
for key , value in table.items():
    print(key , value)


input= idARRAY
input.append('$')
#N=np V=vp Q=verb P=pro D=det M=nom O=noun
production =[ "S->NV","N->P","P->i","V->QN","N->DM","M->MO","M->O","O->m","O->f","O->t","D->a","Q->p","Q->l","Q->h"]

stack = [0]
index= 0
bool = True
print('Stack    Input    Action    Rule')
while bool:
    data = [str(stack), " ".join(input)]
    if (stack[-1] == '' ):
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
        for i in tokenized:
            if 'tea' in tokenized:
                if 'hate' in tokenized:
                    print("Its not the a good thing to hate. Tea is good for mental health")
            if 'prefer' in tokenized:
                if 'morning' in tokenized:
                    print("Morning flights are always preferred, I dont know why")
            if 'prefer' in tokenized:
                if 'tea' in tokenized:
                    if 'flight' in tokenized:
                        print("Hi Tea is always preferred in flight")
            if int(tokenized.count('tea')) == 2:
                print('Excursiveness of anything is not good')
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
        print(data[0] + " " + Curr_input + " " + data[2])
    elif (element[0] == 'r' or element[0] == 'R'):
        print('Reducing')
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
        print('Stack is :',stack)
        data.append(table[previousToTerminal][appendedTerminal])
        print(data[0] + " " + Curr_input + " " + data[2] + " ")


