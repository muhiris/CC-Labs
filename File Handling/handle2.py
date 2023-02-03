
f = open("src2.txt", "rt")
check = ['\n','\t','(',')','{','}','%','[',']','++','--','*=','+','-','<','>','!','!=','>=','<=','>>','<<','&&','&','=']
a= []
temp =''
for itm in f:
 for each in itm:
     if each in check:
         temp +='#'
     temp += each
    
        



print(temp)
      


        
    