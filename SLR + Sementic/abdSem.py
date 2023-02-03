file = open('input.txt','rt')

store=''
mainList=[]
def isfloat(num):
    try:
        float(num)
        return True
    except ValueError:
        return False
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

            
        
    else:
        store=store+char

file.close()    
print(mainList) 
print("corrected without comma")
newMain = []

     
for index , x  in  enumerate(mainList) :
   for  ind,i in enumerate(x) :
       if (i==','):
        
          print(x[0:1])
          print(x[1:]) 
          mainList[index] = x[0:1] 
          mainList[index+1] = x[1:] 
print(mainList)
          




print("verfied")
idARRAY = []
for index , x  in  enumerate(mainList) :
  if(x.isalpha() and x!= 'int'):
    idARRAY.append('i')
  elif(x.isdigit()):
      idARRAY.append('r')
      
  else:
   if(not isfloat(x)):  
    idARRAY.append(x)
# printing accepted array
print(idARRAY)
# /////////////////sementic array making
SementicARRAY = []
for index , x  in  enumerate(mainList) :
  if(x.isalpha() and x!= 'int'):
    SementicARRAY.append(x)
  elif(x.isdigit()):
      SementicARRAY.append(x)
      
  else:
   if(not isfloat(x)):  
    SementicARRAY.append(x)
# printing accepted array
print("SementicARRAY")
print(SementicARRAY)
# /////////////////sementic array making off

print("readed table in array form")
with open('table.txt' ,'r') as obj:
    listable = [[y.replace('Â\xa0','') for y in x.split(',')] for x in obj.read().split('\n') if x!= ''  ]
print(listable)
# Parsing From following Table

table = {}
terminals =['=' ,'-' ,'+' ,'(' ,')' ,'r' ,'i' ,'$']  #lets take r for digits and i for indexes
non_terminals =['S' ,'E' ,'T' ,'F','V']

for index , value in enumerate(listable):
    table[index] ={}
    for ind, val in enumerate(terminals +non_terminals):
        table[index][val] = value[ind]
print("Table Dictionary")
print(table)
# ////////////////////////////////////////// Sementics Value Function \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\ #
S_val=''
E_val=''
T_val=''
F_val=''
V_val=''

def Sementics_Values(rule_no):
	global S_val, E_val, T_val, F_val, V_val, previousIndex

	if rule_no == 0:
		S_val = str(E_val)
		V_val = str(E_val)
		result= "S.val = "+ str(S_val) 
		return result
	elif rule_no == 1:
		E_val = ' '.join([str(E_val), '+', str(T_val)])
		result= "E.val = "+str(E_val)
		return result
	elif rule_no == 2:
		E_val = str(T_val)
		result= "E.val = "+ str(E_val) 
		return result
	elif rule_no == 3:
		T_val = ' '.join([str(T_val), '*', str(F_val)])
		result= "T.val = "+str(T_val)
		return result
	elif rule_no == 4:
		T_val = F_val
		result= "T.val = "+str(T_val) 
		return result
	elif rule_no == 5:
		F_val = E_val
		result= "F.val = "+ str(F_val)
		return result
	elif rule_no == 6:
		F_val = previousIndex
		result= "F.val = "+ str(F_val)
		return result
	elif rule_no == 7:
		a=idARRAY.index('i')
		V_val = SementicARRAY[a]
		result= "V.val = "+str(V_val)
		return result
	else:
		print("Sorry Wrong Sementic Reached")
# ////////////////////////////////////////// Sementics Value Function Out \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\ #

    

input  = idARRAY
production =[ "S->V=E",
"E->E-T",
"E->T",
"T->T+F",
"T->F",
"T->(E)",
"F->r",
"V->i"]
# print( f"production {len(production[0]-3)}")
sementics = ["S.val = E.val; V.val = E.val; print(S.val)" ,"E.val = E1.val - T.val" ,"E.val = T.val" ,"T.val = T.val + F.val" ,"T.val = F.val" ,"F.val = E.val" ,"F.val = digit.lexval" ,"V.val =id.lexval"]



input.append('$')

stack = [0]
index= 0
bool = True
# Heading 
gap = ' '*3
heading = f"{'Stack':40s}{gap}{'Input':40s}{gap}{'Action':6s}{gap}{'Rule':30s}"
print("="*126)
print(heading)
print("-"*126)
# Heading Out
while bool:
    data = [" ".join(str(stack))," ".join(input)]
    if(stack[-1] ==''):
        print("////////Error\\\\\\\\ ====  " ,end="")
        print('got null value  unParsable')
        
        break
        
    Top_Stack = int(stack[-1])
    Curr_input = input[index]
 
    
   
    # element is production number Rx Sx or accept
    try:
     element =table[Top_Stack][Curr_input] 
    except:
        print("error do not pass")

    # final condition when acceptes happens
    if (element=='acc'):
        print("congrats accepted")
        break
    if (element[0]=='s' or element[0]=='S' ):

        stack.append(Curr_input)
        temp = ""
        for x in range(1 ,len(element)):
            temp += element[x]
        stack.append(temp)
        index +=1
        previousIndex = SementicARRAY[index-1]
    
        data.append(element)
        rec = f"{data[0]:40s}{gap}{data[1]:40s}{gap}{data[2]:6s}{gap}"
        print(rec)
    elif (element[0]=='r' or element[0]=='R' ):
          prodlen =len(production[int(element[1:])]) -3 # -1 stands for as our production array is 0  1   2  not   1   2   3
                                                         # where -3 is for terminating length A->
          em_rule=str(Sementics_Values(int(element[1:])))
        
        #   print('Operation **Reduction**')
       
        #   first step was pop
        #   print("stack=  " ,end="")
          
          for i in range(prodlen*2):
            try:  
             stack.pop()
            except:
                print("*//// Error \\\\\\\\*")
                print("There is error more pops then elements present")
                bool =False
                break
          if(bool==False):
              break      
        #   append that terminal symbol you reduced with
          stack.append((production[int(element[1:])])[0])
          after_red = int(stack[-2])   #left most element as others are popped already
          Top_Stack_reduced = (stack[-1])  #right most terminal symbol
        #   adding that goto value
          stack.append(table[after_red][Top_Stack_reduced])
    
          data.append(table[after_red][Top_Stack_reduced])
          data.append(em_rule)
          rec = f"{data[0]:40s}{gap}{data[1]:40s}{gap}{data[2]:6s}{gap}{data[3]:30s}"
          print(rec)
