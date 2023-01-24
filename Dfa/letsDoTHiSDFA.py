obj = open("dfa.txt", 'r')
readFile = obj.read().split('\n')
transitions = []

print('step 1')
print(readFile)
print('step 2')

for x in readFile:
    transitions.append(x.split(' '))
print(transitions)

print('step 3')

for i in range(len(transitions)):
    for j in range(len(transitions[i])):
       if transitions[i][j] != '-':
        transitions[i][j] = int(transitions[i][j])
print(transitions)

print('step 4')

readAlphabet = open("alphabet.txt", 'r')
alph = []
index = 0
for x in readAlphabet.read().split('\n'):
    x += f" {index}"
    print(x)
    alph.append(x.split())
    index += 1

print(alph)

        
print('step 5')
print('Please! register your input')
inputt = '10101' 
current_state = 0
for i in range(len(inputt)):
    for x in alph:
        if inputt[i]==x[0]:
            c = int(x[1])
    print(f"going for transaction on state {current_state} by input {x[0]} jumps on {transitions[current_state][c]} ")
    if(transitions[current_state][c]!='-'):
     current_state = transitions[current_state][c]
    else:
        current_state = transitions[current_state][c]  #'-'
        break
        
print(f"Final State {current_state}")
final_state = [2,3]
if current_state in final_state:
    print("success")
else:
    print('failed again')
        