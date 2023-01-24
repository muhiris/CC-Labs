
NON_TERMINAL = ["S","E","C","T","Y",'F']
TERMINAL = ["I","-","+","*","(",")","$"]
STACK = ["S"]

def push(data):
    STACK.pop()
    data.reverse()
    for i in data:
        STACK.append(i)
    
def Tabel(rowIndex,colIndex):
    col = TERMINAL
    row = NON_TERMINAL
    Tabel = [
        [[],[],[],["E$"],[],["E$"]],
        [[],[],[],[],[],[]],
        [[],[],[],[],[],[]],
        [[],[],[],[],[],[]]
    ]

    return Tabel[row.index(rowIndex)][col.index(colIndex)]



def StartProgram():
    inputData = "i+i&"
    index = 0
    while index < len(inputData):
        print(STACK)
        currentValue = inputData[index]
        TopOfTheStack = STACK[-1]
        if TopOfTheStack in TERMINAL and currentValue != TopOfTheStack:
            break
        elif TopOfTheStack in TERMINAL and currentValue == TopOfTheStack:
            index+=1
            STACK.pop()
            continue
        productionValue= Tabel(TopOfTheStack,currentValue)
        if len(productionValue) == 0:
            break
        elif len(productionValue) == 1 :
            if productionValue[0] =="-":
                STACK.pop()
            continue
        push(productionValue)
    if index < len(inputData):
        print("INVALID INPUT")

StartProgram()