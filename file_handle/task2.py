#alphabets = -1
#numbers = -2
#symbols = 0,8
#repeatSymbols=14,19
#spaces = -3
# / = -5 ignorance check

import time
st = time.time()

def ret_symbol_no(Char, symbols ):
    
    if Char.isalpha() == True or Char == '_':
        return -1
        
    elif Char.isnumeric() == True:
         return -2
        
    elif Char == " ":
        return -3
    
    elif Char == '\\':
        return -4
        
    elif Char =='\n' or Char == '\t' or Char == '\a':
        return -5
        
    for i in range(len(symbols)):
        if Char == symbols[i]:
            return i

def tokenize(line):
    tokens=[]
    symbols=['[',']','#','{','}','\\','%','(',')',',','.',';','"',"'",'<','>','=','+','-','*',':','!','/','&','|'] #RC after 14 15-19

    word=''
    i=0
    while(i<len(line)):
        
        JMP=False
        code=(ret_symbol_no(line[i], symbols))
        
        if code == -1 or code==-2:
            word=word+line[i]
            if (i == len(line)-1):
                if not word=="":
                    tokens.append(word)
                
        
        elif code > -1:
            if code <14:
                if not word=="":
                    tokens.append(word)
                tokens.append(symbols[code])
                
            else:
                if (i+1 < len(line) ):
                    code2 = (ret_symbol_no(line[i+1], symbols))
                    if not code2 < 14:
                        sym=line[i]+line[i+1]
                        if not word=="":
                            tokens.append(word)
                        tokens.append(sym)
                        JMP = True
                    else:
                        if not word=="":
                            tokens.append(word)
                        tokens.append(symbols[code])
                        
                else:
                    if not word=="":
                        tokens.append(word)
                    tokens.append(symbols[code])
            word=''
                        
                
        elif code == -3:
            if not word=="":
                tokens.append(word)
            word=''
        
        
        elif code == -4:
            if (i+1 < len(line) ):
                NextChar=line[i+1]
                if  NextChar == 'n' or NextChar == 't' or NextChar == 'a':
                    if not word=="":
                        tokens.append(word)
                    JMP = True
                
                else:
                    if not word=="":
                        tokens.append(word)
                    tokens.append(line[i])
                    
            else:
                if not word=="":
                    tokens.append(word)
                tokens.append(line[i])    
                
            word=''
            
        
        elif code == -5:
            if not word=="":
                tokens.append(word)
            word=''
        
        if JMP == True:
            i=i+2
        else:
            i=i+1
                
    print(tokens)
    



f1= open("C:/Users/Abdullah/Desktop/test/Compiler Construction/file_handle/src2.txt", "r")
listf1=f1.readlines()

for i in listf1:
    (tokenize(i))
    
tokenize("int x+=5;")

print('Execution time:', time.time() - st, 'seconds') 