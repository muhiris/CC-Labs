table = {
    "E":{"i":"TX","*":"","+":"","(":"TX",")":"","$":""},
    "X":{"i":"", "*":"", "+":"+E", "(":"", ")":"-", "$":"-"},
    "T":{"i":"iY", "*":"", "+":"", "(":"(E)", ")":"", "$":""},
    "Y":{"i":"", "*":"*T", "+":"-", "(":"", ")":"-", "$":"-"}
}

inp = input("Enter the input String")
stack = ["$","E"]
in_cursor = 0
push=[]
pop=[]
print("Stack            Input           cursor          PUSH            POP")
while True:
    push=[]
    pop=[]    
    if (len(stack)==0 and not in_cursor>(len(inp)-1)) or (len(stack)!=0 and in_cursor>(len(inp)-1)):
        print("Error")
        break
    elif len(stack)==0 and in_cursor>(len(inp)-1):
        print("Successfull")
        break
    else:
        if inp[in_cursor]==stack[-1]:
            popString = "POP("+stack[-1]+")"
            pop.append(popString)
            stack.pop()
            in_cursor+=1
        elif stack[-1]=="-":
            popString = "POP("+stack[-1]+")"
            pop.append(popString)
            stack.pop()
            
        else:
            new_push = table[stack[-1]][inp[in_cursor]]
            popString = "POP("+stack[-1]+")"
            pop.append(popString)
            stack.pop()
           
            if len(new_push)>1:
                for i in new_push[::-1]:
                    pushString = "PUSH("+i+")"
                    push.append(pushString)
                    stack.append(i)
            else:
                stack.append(new_push)
                pushString = "PUSH("+new_push+")"
                push.append(pushString)
            
    print(stack,"           ",inp,"          ","          ",in_cursor,"         ",push,"       ",pop)