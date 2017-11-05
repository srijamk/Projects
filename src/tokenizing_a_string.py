class Tokenizing():
    def tokenize_string(self, string):
        operators = ["+", "-", "/", "*", "^", "(", ")"]
        token_list = []
        for char in string:
            if char in operators and (char == "+" or char == "-"):
                if string[string.index(char) - 1] == " " and string[string.index(char) + 1] == " ":
                    token_list.append(char)
            elif char in operators and not(char == "+" or char == "-"):
                token_list.append(char)

        return token_list

if __name__ == '__main__':
    string = raw_input("Enter a string: ")
    print Tokenizing().tokenize_string(string)
