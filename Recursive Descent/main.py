inp_pointer = 0
desc_pointer = 0
stack = ['S']
question = open('input.txt','r')
data = question.readline()
print(data)
grammar_rules = [
    ['S', ['c', 'A', 'd']],
    ['A', ['a', 'b']],
    ['A', ['a']]
]
#continue until stack gets empty

if stack[0].isupper():
    if data[inp_pointer] == grammar_rules[0][1][0]:
        stack.pop(0)
        stack.insert(0, grammar_rules[0][1][1])
        stack.insert(0, grammar_rules[0][1][2])
        print(stack)
        inp_pointer += 1
        print(inp_pointer)
    elif data[inp_pointer] == grammar_rules[1][1][0]:
        stack.pop(0)
        stack.insert(0, grammar_rules[1][1][1])
        print(stack)
        inp_pointer += 1
        print(inp_pointer)
    elif data[inp_pointer] == grammar_rules[2][1][0]:
        stack.pop(0)
        print(stack)
        inp_pointer += 1
        print(inp_pointer)
    else:
        print("Error")
elif stack[0].islower():
    if data[inp_pointer] == stack[0]:
        stack.pop(0)
        inp_pointer += 1
        print(inp_pointer)
    else:
        print("Error")


