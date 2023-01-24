from asyncio.windows_events import NULL


f = open("C:/Users/Abdullah/Desktop/test/Compiler Construction/file_handle/src2.txt", "rt")
check = ['\n','\t','(',')','{','}','%','[',']','++','--','*=','+','-','<','>','!','!=','>=','<=','>>','<<','&&','&','=']
a= []
temp =''
for itm in f:
 for each in itm:
     if each in check:
         temp +='#'
     temp += each
    
        



print(temp)
      


        
    