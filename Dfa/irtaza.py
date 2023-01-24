states  = [0,1,2,3]
currentState  = states[0]
currentindex =0

str  = input("enter your string to pass \n")

print(len(str) )

a =[str[i:i+4] for i in range(0, len(str), 4)]
print(a)


for i in range(len(a)):
    print(i)
    if(len(a[i])>0):
        if (a[i][0] =='a' ):
            currentState =(states[1])
        if (a[i][0]=='b'):
            currentState=(states[0])
    else:
        break
    if(len(a[i])>1):
        if (a[i][1]=='a'):
            currentState=(states[1])
        if (a[i][1]=='b'):
            currentState=(states[2])
    else:
        break
    if(len(a[i])>2):
        if (a[i][2]=='a'):
            currentState=(states[1])
        if (a[i][2]=='b'):
            currentState=(states[3])
    else:
        break
    if(len(a[i])>3):
        if (a[i][3]=='a'):
            currentState=(states[1])
        if (a[i][3]=='b'):
            currentState=(states[0])
    else:
        break
if currentState == 3:
    print('success')
else:
    print('failed')
    print(currentState)







    
 