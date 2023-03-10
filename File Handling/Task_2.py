
# Reading from the file
read_obj = open('src2.txt', 'r')
code = read_obj

# Initializing lists
ignoreList = [' ', '\t', '\n']
operatorList = [';', ':', '(', ')', '[', ']',
                '{', '}', '"', "'", ",", '.', '#']
operationsList = ['+', '-', '*', '/', '=']
comparisonList = ['>', '<', '!', '=']

# Converting tokens into an array
tokens = []
string = ""


def checkOperation(char, string, operator):
    if string != "":
        tokens.append(string)
    string = char
    char = code.read(1)
    if operator == "operations":
        list = operationsList
    else:
        list = comparisonList

    if char in list:
        if operator == "comparison":
            list1 = ['<', '>']
        else:
            list1 = ["*", "/"]
        if string == char:
            if operator == "comparison":
                if string == char == "!":
                    # syntax error
                    print('Error compiling the code!')
                    exit()
            string += char
            tokens.append(string)
            string = ""
        elif char == "=":
            string += char
            tokens.append(string)
            string = ""
        elif char in list1:
            print("Error compiling the code!")
            exit()
        else:
            tokens.append(string)
            tokens.append(char)
            string = ""
    else:
        tokens.append(string)
        string = ""
        if char != ' ':
            string = char
    return [char, string]


# reading file char by char
while 1:
    char = code.read(1)
    # If file is empty or EOF
    if not char:
        break
    # File not empty or !EOF
    else:
        # if the char is not a SPACE, an EOL, or a TAB
        if char not in ignoreList:
            # in case of comments, combine the whole comment into one token
            if char == "#":
                if string != "":
                    tokens.append(string)
                    string = char
                string = char
                while 1:
                    char = code.read(1)
                    if char == "\n":
                        tokens.append(string)
                        string = ""
                        char = code.read(1)
                        break
                    else:
                        string += char
            if char in operationsList:
                [char, string] = checkOperation(char, string, 'operations')
            elif char in comparisonList:
                [char, string] = checkOperation(char, string, 'comparison')
            elif char in operatorList:
                if string != "":
                    tokens.append(string)
                    string = ""
                tokens.append(char)
            else:
                string += char
        # if the char is a SPACE, an EOL, or a TAB
        else:
            if string != "" and string != " ":
                tokens.append(string)
                string = ""
print(tokens)
