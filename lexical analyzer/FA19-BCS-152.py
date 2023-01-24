file = open('src.txt','rt')

escape = [' ',';','\n','\t','(',')','{','}','%','[',']',"++","--","*=",'+','-','<','>','!',"!=",">=","<=",">>","<<","&&","&"]
variable_transitions = [['1','1','-','1','-','-','-','-','-'],['1','1','1','1','-','-','-','-','-']]
digit_transitions = [['-','-','1','-','-','-','-','-','-'],['-','-','1','-','-','-','-','-','-']]
float_transitions = [['-','-','1','-','-','-','-','-','-'],['-','-','1','-','2','-','-','-','-'],['-','-','3','-','-','-','-','-','-'],['-','-','3','-','-','-','-','-','-']]
string_transitions = [['-','-','-','-','-','1','-','-','-'],['1','1','1','1','1','2','1','1','1'],['-','-','-','-','-','-','-','-','-']]
singleComment_transitions = [['-','-','-','-','-','-','1','-','-'],['-','-','-','-','-','-','2','-','-'],['2','2','2','2','2','2','2','2','3'],['-','-','-','-','-','-','-','-','4'],['-','-','-','-','-','-','-','-','-']]

# KeyWords
keywords = [
    "auto",
    "bool",
    "break",
    "case",
    "catch",
    "char",
    "word",
    "class",
    "const",
    "continue",
    "delete",
    "do",
    "double",
    "else",
    "enum",
    "false",
    "float",
    "for",
    "goto",
    "if",
    "#include",
    "int",
    "long",
    "namespace",
    "not",
    "or",
    "private",
    "protected",
    "public",
    "return",
    "short",
    "signed",
    "sizeof",
    "static",
    "struct",
    "switch",
    "true",
    "try",
    "unsigned",
    "void",
    "while"
]


def multipleCurrentStates(current_state,current_input):
    next_state =""
    temp = current_state.split(",")
    for j in temp:
        if j!="-":
            temp_next_state = transitions[int(j)][int(current_input)]
            if temp_next_state !="-":
                if len(temp_next_state)==1:
                    next_state+=temp_next_state
                    next_state+=","
                elif len(temp_next_state)>1:
                    next_state+=multipleNextStates(temp_next_state)
    if next_state!= "":
        if next_state[-1]==",":
            next_state = next_state[:-1]
            
    return next_state
        


def nfa(current_state, final_state,input_string, transitions):
    for i in range(len(input_string)):
        if current_state != '-': 
            if len(current_state)==1:
                next_state = transitions[int(current_state)][int(input_string[i])]
                if i!= (len(input_string)-1):
                    if len(next_state) > 1:
                        current_state = multipleNextStates(next_state)
                    else:
                        current_state = next_state
                elif i==(len(input_string)-1):
                    if len(final_state) >1:
                        temp = final_state.split(",")
                        for k in temp:
                            if k in next_state.split(","):
                                return True
                    elif len(final_state)==1 and final_state in next_state.split(","):
                        return True
                    else:
                        return False
                        
            elif len(current_state)>1:
                next_state = multipleCurrentStates(current_state, input_string[i])
                if i!= (len(input_string)-1):
                    if len(next_state) > 1:
                        current_state = multipleNextStates(next_state)
                elif i==(len(input_string)-1):
                    if len(final_state) >1:
                        temp = final_state.split(",")
                        for k in temp:
                            if k in next_state.split(","):
                               return True
                    elif len(final_state)==1 and final_state in next_state.split(","):
                       return True
                    else:
                        return False
        else:
            return False

                           



a=[]
temp =""
flag = False
for i in file:
    for j in i:
        if flag == False and j == '"':
            flag = True
        elif flag == True and j == '"':
            flag = False
            temp+=j
            a.append(temp)
            temp =""
        if flag == False:
            if j not in escape:
                temp+=j
            elif j==" ":
                a.append(temp)
                temp =""
            elif j !=" " and j!='\n' and j!='\t' and j in escape:
                a.append(temp)
                a.append(j)
                temp =""
        else:
            temp+=j
        

strings=[]
variables=[]
digits=[]
floats=[]
singleComments=[]


for e in a:
    if not e in keywords:
        input_string = ""
        for i in e:
            if ord(i)>=65 and ord(i)<=90:
                input_string+='1'
            elif (ord(i)>=97 and ord(i)<=122):
                input_string+='0'
            elif (ord(i)>=48 and ord(i)<=57):
                input_string+='2'
            elif i=='_':
                input_string+='3'
            elif i=='.':
                input_string+='4'
            elif i=='"':
                input_string+='5'
            elif i=='/':
                input_string+='6'
            elif i=='*':
                input_string+='7'
            elif i=='\\':
                input_string+='8'
        if nfa('0', '1',input_string, variable_transitions): # current + final
            variables.append(e)
        elif nfa('0', '1',input_string, digit_transitions):
            digits.append(e)
        elif nfa('0', '3',input_string, float_transitions):
            floats.append(e)
        elif nfa('0', '2',input_string, string_transitions):
            strings.append(e)
        elif nfa('0', '4',input_string, singleComment_transitions):
            singleComments.append(e)



print("Digits: ",digits)
print("Strings: ",strings)
print("Float: ",floats)
print("Variabales: ",variables)
print("single Line Comments: ",singleComments)



def multipleNextStates(next_state):
    current_state = ""
    temp = next_state.split(",")
    for j in temp:
        if j!="-":
            current_state+= (j+",")
    current_state = current_state[:-1]
    return current_state




            
