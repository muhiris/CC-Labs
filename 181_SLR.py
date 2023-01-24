table = {
    # C denotes E` and Y denotes T`
    0:
        {"a": "S3", "b": "S4", "$": "", "A": "2", "S": "1"},

    1:
        {"a": "", "b": "", "$": "Accept", "A": "", "S": ""},

    2:
        {"a": "S3", "b": "S4", "$": "", "A": "5", "S": ""},

    3:
        {"a": "S3", "b": "S4", "$": "", "A": "6", "S": ""},

    4:
        {"a": "R3", "b": "R3", "$": "R3", "A": "", "S": ""},

    5:
        {"a": "R1", "b": "R1", "$": "R1", "A": "", "S": ""},
    6:
        {"a": "R2", "b": "R2", "$": "R2", "A": "", "S": ""},
}

input = ['a', "a", "b", "b"]
stack= [0]
pointer = 0
input.append('$')
production = ['S->AA', 'A->aA', 'A->b']


def reduce():
    # Reduction function for SLR comments
    # 1. Pop the top of the stack according to rule. if rule has 2 characters then pop 4 times
    # 2. Append the non terminal symbol of that rule to the stack
    # 3. Append the next state to the stack

    # As our production array is 0 1 2 not 1 2 3 so subtracting 1. i.e. for R1 it is 0
    print('\nApplying Reduction: ', end=" ")
    ruleNo = production[int(element[1]) - 1]
    # each production has 3 characters of terminal symbol so subtracting 3 i.e. for 'X' '-' '>' it is 3
    extraLen = 3
    prodleng = len(ruleNo) - extraLen

    for i in range(prodleng * 2):
        stack.pop()
    #   appending terminal symbol you reduced with
    stack.append(ruleNo[0])

    appendedTerminal = (stack[-1])
    previousToTerminal = int(stack[-2])
    #   adding that goto value
    stack.append(table[previousToTerminal][appendedTerminal])

def shift():
    #  Shift function appends the current input and the next state i.e.
    #  if at 'a' there is 'S2' then you have to first append 'a' and then '2'
    #  to the stack. After that move the current input (which was 'a') to the next
    #  input (which is 'a' in this case)
    global pointer
    global stack
    print("\nApplying Shift: ", end=" ")
    stack.append(current_input)
    stack.append(int(element[1]))
    pointer += 1




while True:
    stack_top = int(stack[-1])
    current_input = input[pointer]
    print(stack_top,end=" ")
    print(current_input,end=" ")
    element = table[stack_top][current_input]
    if (element == 'Accept'):
        print("\n\nBoom! Accepted")
        break
    if (element == ''):
        print("\n\nError")
        break
    if (element[0] == 'S'):
       shift()

    elif (element[0] == 'R'):
       reduce()

    else:
        print("\n\nError")
        break
