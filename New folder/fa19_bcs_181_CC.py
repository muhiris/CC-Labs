import re
import mysrc


def basicCheck(token):
    varPtrn = re.compile(r"[a-zA-Z_][a-zA-Z0-9_]")  # variables
    headerPtrn = re.compile(r"\w[a-zA-Z]+[.]h")  # header files
    digitPtrn = re.compile(r'\d')
    floatPtrn = re.compile(r'\d+[.]\d+')

    if token in mysrc.keywords():
        print(token + " KEYWORD")
    elif token in mysrc.operators().keys():
        print(token + " ", mysrc.operators()[token])
    elif token in mysrc.delimiters():
        description = mysrc.delimiters()[token]
        if description == 'TAB' or description == 'NEWLINE':
            print(description)
        else:
            print(token + " ", description)
    elif re.search(headerPtrn, token):
        print(token + " HEADER")
    elif re.match(varPtrn, token) or "'" in token or '"' in token:
        print(token + ' IDENTIFIER' )
    elif re.match(digitPtrn, token):
        if re.match(floatPtrn, token):
            print(token + ' FLOAT')
        else:
            print(token + ' INT')

    return True

def delimiterCorrection(line):
    tokens = line.split(" ")
    for delimiter in mysrc.delimiters().keys():
        for token in tokens:
            if token == delimiter:
                pass
            elif delimiter in token:
                pos = token.find(delimiter)
                tokens.remove(token)
                token = token.replace(delimiter, " ")
                extra = token[:pos]
                token = token[pos + 1 :]
                tokens.append(delimiter)
                tokens.append(extra)
                tokens.append(token)
            else:
                pass
    for token in tokens:
        if isWhiteSpace(token):
            tokens.remove(token)
        elif ' ' in token:
            tokens.remove(token)
            token = token.split(' ')
            for d in token:
                tokens.append(d)
    return tokens

def isWhiteSpace(word):
    ptrn = [ " ", "\t", "\n"]
    for item in ptrn:
        if word == item:
            return True
        else:
            return False

#def hasWhiteSpace(token):
    ptrn = ['\t', '\n']
    if isWhiteSpace(token) == False:
        for item in ptrn:
            if item in token:
                result = "'" + item + "'"
                return result
            else:
                pass
    return False

def tokenize(path):
    try:
        f = open(path).read()
        lines = f.split("\n")
        count = 0
        for line in lines:
            count = count + 1
            tokens = delimiterCorrection(line)
            print("\n#LINE ", count)
            print("Tokens: ", tokens)
            for token in tokens:
                basicCheck(token)
        return True
    except FileNotFoundError:
        print("\nInvald Path. Retry")
        run()

def run():
    path = input("Enter Source Code's Path: ")
    tokenize(path)
    again = int(input("""\n1. Retry\n2. Quit\n"""))
    if again == 1:
        run()
    elif again == 2:
        print("Quitting...")
    else:
        print('Invalid Request.')
        run()

run()