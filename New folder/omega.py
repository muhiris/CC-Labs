from numpy import arange


file  = open('src.txt' , 'r')

temp= ''
array = []


while True:
    char  = file.read(1)
    
    if not char :
        if temp!='':
          array.append(temp)
        break
    elif (char=='\t' or char=='\n' or char== ' '):
      if temp!='':
          array.append(temp)
      temp = ''
    elif (char == '+' or char == '-' or char == '*' or char == '/' or char == '='):
       if temp!='':
          array.append(temp)
       temp = ''
       if (char != file.read(1)):
          array.append(char)
       else:
         array.append(char+char)
       file.read(0)
    else:
      temp = temp+char
print(array)
    
        
      