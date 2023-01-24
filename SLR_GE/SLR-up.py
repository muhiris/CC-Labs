# semantic = [code,place]
# GRAMMAR:
#  S -> id := E 
#  E -> E + E | E * E | -E | ( E ) | id 
# -E -> 

# AUGMENTED GRAMMAR:
# 0: S' -> S 
# 1:  S -> id := E 
# 2:  E -> E + E 
# 3:  E -> E * E 
# 4:  E -> -E 
# 5:  E -> ( E ) 
# 6:  E -> id 

# TERMINALS   : ['id', ':=', '+', '*', '(', ')']
# NONTERMINALS: ["S'", 'S', 'E', '-E']
# SYMBOLS     : ["S'", 'S', 'E', '-E', 'id', ':=', '+', '*', '(', ')']
# PARSING TABLE:
# +--------+--------+--------+--------+--------+--------+--------+--------+--------+--------+--------+
# | STATE  |   id   |   :=   |    +   |    *   |    (   |    )   |    $   |    S   |    E   |   -E   | 
# +--------+--------+--------+--------+--------+--------+--------+--------+--------+--------+--------+
# |   0    |   s2   |        |        |        |        |        |        |    1   |        |        | 
# |   1    |        |        |        |        |        |        |   acc  |        |        |        | 
# |   2    |        |   s3   |        |        |        |        |        |        |        |        | 
# |   3    |   s6   |        |        |        |   s7   |        |        |        |    4   |    5   | 
# |   4    |        |        |   s8   |   s9   |        |        |   r1   |        |        |        | 
# |   5    |        |        |   r4   |   r4   |        |   r4   |   r4   |        |        |        | 
# |   6    |        |        |   r6   |   r6   |        |   r6   |   r6   |        |        |        | 
# |   7    |   s6   |        |        |        |   s7   |        |        |        |   10   |    5   | 
# |   8    |   s6   |        |        |        |   s7   |        |        |        |   11   |    5   | 
# |   9    |   s6   |        |        |        |   s7   |        |        |        |   12   |    5   | 
# |   10   |        |        |   s8   |   s9   |        |   s13  |        |        |        |        | 
# |   11   |        |        |  r2/s8 |  r2/s9 |        |   r2   |   r2   |        |        |        | 
# |   12   |        |        |  r3/s8 |  r3/s9 |        |   r3   |   r3   |        |        |        | 
# |   13   |        |        |   r5   |   r5   |        |   r5   |   r5   |        |        |        | 
# +--------+--------+--------+--------+--------+--------+--------+--------+--------+--------+--------+

newTemp = 0
def newtemp():
    global newTemp
    newTemp += 1
    return "t" + str(newTemp)
def gen(s):
    for i in range(1,s):
    temp = newtemp()
    print("Semantic Grammer: " + s)
    if s == 1:
        print("T1 := d*f T2=c+T1 T3:=b+T2 T4:=a+T3")
    elif s == 2:
        print("T2=c+T1")
    elif s == 3:
        print("T3:=b+T2")
    elif s == 4:
        print("T4:=a+T3")
        
    
def match(t):
    if t == token:
        next()
    else:
        error()
def next():
    global token
    token = input()
def error():
    print("Error")
def table():
    f = open("table.txt")
    table = []
    for line in f:
        
        lines = line.strip().split(",")
        table.append(lines)
    return table

table = table()
print("Table is:\n",table)
ques = ['a','a','b','b']
currentLocation = 0
# stack = ques[::-1]
stack = ques
# pointer = 0
print(stack.pop())
# slr parser
for i in range(0,6):
    for j in range(0,5):
        if table[i][j][0] == 'S':
            for k in range(6):
                try:
                    if table[i][j][1] == str(k):
                        print("Shifted ",table[i][j])
                        # pointer += 1
                        stack.pop()
                        currentLocation = j
                
                except:
                    continue

        if table[i][j][0] == 'R':
            for k in range(6):
                try:
                    if table[i][j][1] == str(k):
                        print("Reduced ",table[i][j])
                        
                
                except:
                    continue
        for k in range(7):
            if table[i][j] == str(k):
                print("Moved to ",table[i][j])
                currentLocation = j
                
        if table[i][j] == "-":
            continue

        if table[i][j] == "acc":
            print("Accepted")
            break
if(table[i][j] == "acc"):
    gen(1)
elif (table[i][j] == "-"):
    gen(2)
elif (table[i][j] == "r1"):
    gen(3)
elif (table[i][j] == "r2"):
    gen(4)
elif (table[i][j] == "r3"):
    gen(5)
elif (table[i][j] == "s2"):
    gen(6)