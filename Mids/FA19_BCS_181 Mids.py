#FA19_bcs_146 7C #CC
# LAB MID
# ABDULLAH ALI


from numpy import number


file = open('input.txt','rt')
raw = open('input.txt','rt')

store=''
mainList=[]
# TOKENIZE
print('\n')
print('identified')
print('\n')
print(raw.read().split())
while 1:
    char = file.read(1)
    if not char:
        #if the end is empty or store is, Don't append
        if(store!=''):
            mainList.append(store)
        break
    # if space, new line add the previous word to list
    elif (char==' ' or char=='\n' or char=='\t'):
        if(store!=''):
            mainList.append(store)
        store=''
    # if +,-,*,/ append it to the list too    
    elif (char=='+'  or char=='*' or char=='(' or char==")"):
        
        
            if(store!=''):
                mainList.append(store)
            store=''
            mainList.append(char)
                    
   
            
        
    else:
        # only accepting numbers here
       try:
        
        store=store+str(int(char))
       except:
           continue

file.close()    
# CONVERTED INTO ID
for index , x  in  enumerate(mainList) :
  
   try:
    if (int(x)!=False):
        mainList[index] ="I"
   except:
       continue
print('\n')
print('verified')
print('\n')
idARRAY = []
for index , x  in  enumerate(mainList) :
  if(x=='I'):
    idARRAY.append('id')
  else:
    idARRAY.append(x)
# printing accepted array
print(idARRAY)


# Making into String 
print('\n')
print("ID replaced with 'id' Printing String accordingly ")
print('\n')
string = ''
for x in mainList:
    string+=x
print(string)
print('\n')
print('\n')
    
#Parsing the Whole String 


table = {
    # C denotes E` and Y denotes T`
    "S":
        {"$":"","+":"","*":"","(":"E$",")":"","I":"E$"},
    
    "E":
        {"$":"","+":"","*":"","(":"TC",")":"","I":"TC"},
    
    "C":
        {"$":"-","+":"+TC","*":"","(":"",")":"-","I":""},
    
    "T":
        {"$":"","+":"","*":"","(":"FY",")":"","I":"FY"},
    
    "Y":
        {"$":"-","+":"-","*":"*FY","(":"",")":"-","I":""},
    
    "F":
        {"$":"","+":"","*":"","(":"(E)",")":"","I":"I"}
}

inp = string + '$'
stack = ["S"]
in_cursor = 0
print("Stack                  Input                             PUSH                               POP")
while True:
    push=[]
    pop=[]    
    # Conditions which ends the code
    if (len(stack)==0 and not in_cursor>(len(inp)-1)) or (len(stack)!=0 and in_cursor>(len(inp)-1)):
        print("Error not passed")
        break
    elif len(stack)==0 and in_cursor>(len(inp)-1):
        print("Successfull is passed")
        break
    # conditions which maintains stack
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
            if (new_push==''):
                print('error')
                break
                
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
    # Printing according to table
    print(stack,"           ",inp[in_cursor:],"          ","         ",push,"            ",pop)
        
