


table = {
    'E':{'i':'TX' ,'*':'','+':'','(':'TX',')':'','$':''},
    'X':{ 'i':'','*':'','+':'+E','(':'',')':'-','$':'-' },
    'T':{'i':'iY','*':'','+':'','(':'(E)',')':'','$':'' },
    'Y':{'i':'','*':'*T','+':'-','(':'',')':'-','$':'-' }

}

inp = input('enter string')
stack = ['$' , 'E']
in_cursor  = 0

while True:
    if (len(stack)==0 and not in_cursor>(len(inp)-1) or (len(stack)!=0 and in_cursor>(len(inp)-1) ) ):
        print('error')
        break
    elif len(stack) ==0 and in_cursor>(len(inp-1)):
        print('success')
        break
    if inp[in_cursor] ==stack[-1]:
        stack.pop()
        in_cursor+=1
    elif stack[-1]=='-':
        stack.pop()
    else:
        new_push = table[stack[-1]][inp[in_cursor]]
        stack.pop()
        if len(new_push)>1:
            for a in new_push[::-1]:
                stack.append(a)
        else:
            stack.append(new_push)
            