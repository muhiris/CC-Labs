
# Ali Zulqarnain (FA19-BCS-002)
# SLR parser - CC Lab Terminal

import ply.lex as lex


# Class to identify valid tokens and discard invalid tokens
class Tokenize:
    def __init__(self):
        self.tokens = []
        tokens = ('DOLLAR', 'NOUNA', 'NOUNB', 'NOUNC', 'NOUND', 'NOUNE', 'NOUNF', 'NOUNG', 'NOUNH')
        t_DOLLAR = r'\$'
        t_NOUNA = r'i'
        t_NOUNB = r'morning'
        t_NOUNC = r'flight'
        t_NOUND = r'tea'
        t_NOUNE = r'a'
        t_NOUNF = r'prefer'
        t_NOUNG = r'like'
        t_NOUNH = r'hate'

        # Characters to ignore
        t_ignore = '\t\n '

        # In case there is any invalid character
        def t_error(t):
            ind = str(t).find(",'")
            print("Invalid Characters: ", str(t)[ind+2: ind+3])
            t.lexer.skip(1)

        # Create lex object
        self.lexer = lex.lex()

    def tokenize(self, input):

        # Pass the data as input to lex object
        self.lexer.input(input)

        # Iterate over input data
        while True:

            # Separate tokens from input data
            tok = self.lexer.token()

            # End of input
            if not tok:
                break

            self.tokens.append(tok.value)

        return self.tokens


# Main class
class BottomUpParser:
    def __init__(self):
        self.table = {}
        self.readTable = {}
        self.stack = []
        self.annotations_stack = []
        self.input = ''
        self.output = ''
        self.length = {}
        self.Goto = {}
        self.symbols = []
        self.grammar = []
        self.terminals = []
        self.non_terminals = []

    def readingFromFile(self):

        # Remove spaces from input string an append terminating character at the end
        with open('input.txt', 'r') as file:
            inp = file.read().split('\n')
            self.input = inp[0] + '$'

        # Setting grammar productions
        self.grammar = [['S', "AC"], ['A', "B"], ['B', '!'], ['C', "GA"], ["A", "FD"], ["D", "DE"],
                        ['D', 'E'], ['E', '@'], ['E', '#'], ['E', '('], ['F', '%'], ['G', '^'],
                        ['G', '&'], ['G', '*']]

        # Reading table from file
        with open('table.txt', 'r') as file:
            self.readTable = [x.split(',') for x in file.read().split('\n') if x != '']

        # Additional operations on entries of table such as converting empty entries or &nbsp to '-' symbol etc
        self.readTable = [[y.strip().replace('Â\xa0', '-').replace(' ', '-').upper().replace('ACC', 'Accept') if y != ''
                           else '-' for y in x] for x in self.readTable]
        self.readTable = [[y if y != '' else '-' for y in x] for x in self.readTable]

    def tokenizeInput(self):

        # Generate potential tokens from input
        potential_tokens = Tokenize()
        valid_tokens = potential_tokens.tokenize(self.input)

        # Encoding of terminals into special symbols
        converted_tokens = []

        for x in valid_tokens:
            if x == 'i':
                self.symbols.append(x)
                converted_tokens.append('!')
            elif x == 'morning':
                self.symbols.append(x)
                converted_tokens.append('@')
            elif x == 'flight':
                self.symbols.append(x)
                converted_tokens.append('#')
            elif x == 'tea':
                self.symbols.append(x)
                converted_tokens.append('(')
            elif x == 'a':
                self.symbols.append(x)
                converted_tokens.append('%')
            elif x == 'prefer':
                self.symbols.append(x)
                converted_tokens.append('^')
            elif x == 'like':
                self.symbols.append(x)
                converted_tokens.append('&')
            elif x == 'hate':
                self.symbols.append(x)
                converted_tokens.append('*')
            else:
                continue

        print()
        print("Input:", self.input)
        print(f"Potential tokens after discarding invalid tokens: {valid_tokens}")
        self.input = ''.join(map(str, converted_tokens))
        self.input += '$'
        print()

    def setParseTable(self):

        # Indexing grammar productions, finding goto i.e. left side of productions and length of right side of
        # productions (needed to calculate no. of pop operations)
        self.Goto = {}
        self.length = {}
        for index, value in enumerate(self.grammar):
            self.Goto[str(index + 1)] = value[0]
            self.length[str(index + 1)] = int(len(value[1]))

        # Setting terminals and non-terminals (encoded form)
        self.terminals = ['!', '@', '#', '(', '%', '^', '&', '*'] + ['$']
        self.non_terminals = ['S', 'A', 'B', 'C', 'D', 'E', 'F', 'G']

        # Storing parse table in dictionary
        for index, value in enumerate(self.readTable):
            self.table[index] = {}
            self.table[index]['action'] = {}
            self.table[index]['goto'] = {}
            for ind, val in enumerate(self.terminals):
                self.table[index]['action'][val] = self.readTable[index][ind]
            for ind, val in enumerate(self.non_terminals):
                goto = self.readTable[index][len(self.terminals) + ind]
                self.table[index]['goto'][val] = goto if goto == '-' else int(goto)

    def replace(self, inp):
        # Function to decode terminals and non-terminal symbols
        return inp.replace('!', 'i').replace('@', 'morning').replace('#', 'flight').replace('(', 'tea').replace('%',
            'a').replace('^', 'prefer').replace('&', 'like').replace('*', 'hate').replace('A', 'NP').replace('B',
            'Pro').replace('C', 'VP').replace('D', 'Nom').replace('E', 'Noun').replace('F', 'Det').replace('G', 'Verb')

    def parseInput(self):

        gap = ' ' * 3
        print('=' * 105)
        print(f"{'Step':6s}{gap}{'Stack':45s}{gap}{'Input':35s}{gap}{'Action':10s}")
        print('=' * 105)
        step = 1
        index = 0
        inp = self.input

        # Stack needed for parsing the input
        self.stack = [index]

        # A stack to keep track of the parent and child nodes (needed to apply semantic rules)
        while True:
            top = self.stack[-1]
            current_input = inp[index]

            # Check the current input symbol against the state present at top of the stack
            dest = self.table[int(top)]['action'][current_input]

            stck = self.replace(' '.join(map(str, self.stack)))

            potential_tokens = Tokenize()
            valid_tokens = potential_tokens.tokenize(self.replace(inp[index:]))
            inpt = ' '.join(map(str, valid_tokens))

            # In case input is parsed successfully
            if dest == "Accept":
                print(f"{step:<6d}{gap}{stck:45s}{gap}{inpt:35s}{gap}{'Accept':10s}")
                print('-' * 145, end='\n\n')
                print("Output: ", self.output, end='\n')
                print("Input successfully parsed :)")
                potential_tokens = Tokenize()
                valid_tokens = potential_tokens.tokenize(self.replace(self.input))
                self.printRules(' '.join(map(str, valid_tokens)))
                break

            # In case there is a shift operation
            elif dest[0] == "S":
                print(f"{step:<6d}{gap}{stck:45s}{gap}{inpt:35s}{gap}S{dest[1:]:10s}")
                step += 1

                # Updating stack and moving pointer position ahead one step
                self.stack.append(current_input)
                self.stack.append(dest[1:])
                index += 1

            # In case there is a reduce operation
            elif dest[0] == "R":
                print(f"{step:<6d}{gap}{stck:45s}{gap}{inpt:35s}{gap}R{dest[1:]:10s}")
                step += 1

                # Compute the length of right side of production (for pop operations)
                length = dest[1:]
                no_of_pops = self.length[str(int(length) + 1)]

                # Perform pop operations
                for i in range(2 * no_of_pops):
                    self.stack.pop()

                # Append goto non-terminal to the stack
                goto = self.Goto[str(int(length) + 1)]
                self.stack.append(goto)

                # Append goto state to the stack
                goto_state = self.table[int(self.stack[-2])]['goto'][goto]
                self.stack.append(goto_state)

                # Print against the goto statement
                potential_tokens = Tokenize()
                valid_tokens = potential_tokens.tokenize(self.replace(inp[index:]))
                inptt = ' '.join(map(str, valid_tokens))
                print(f"{step:<6d}{gap}"
                      f"{self.replace(' '.join(map(str, self.stack[:-1]))):45s}"
                      f"{gap}{inptt:35s}"
                      f"{gap}{self.stack[-1]:}")
                step += 1

            # In case the expected action is not found against terminal
            else:
                print(f"{step:<6d}{gap}{stck:45s}{gap}{inpt:35s}{gap}Expected terminal "
                      f"{self.replace(inp[index:index + 1])}"
                      f" not found at I{self.stack[-1]:45s}!")
                print('-' * 141, end='\n\n')
                print("Cannot parse input :(")
                break

    def printRules(self, inp):

        message = 0

        if 'tea' in inp and 'hate' in inp:
            message = 1
        if 'prefer' in inp and 'morning' in inp:
            message = 2
        if 'prefer' in inp and 'tea' in inp and 'flight' in inp:
            message = 3
        if inp.count('flight') == 2 or inp.count('tea') == 2 or inp.count('morning') == 2:
            message = 4

        print("Message: ")
        if message == 1:
            print("It's not the a good thing to hate. Tea is good for mental health")
        elif message == 2:
            print("Morning flights are always preferred, I dont know why")
        elif message == 1:
            print("Hi Tea is always preferred in flight")
        elif message == 4:
            print("Excursiveness of anything is not good.")


# Driver function
def main():
    obj = BottomUpParser()
    obj.readingFromFile()
    obj.tokenizeInput()
    obj.setParseTable()
    obj.parseInput()


if __name__ == '__main__':
    main()
