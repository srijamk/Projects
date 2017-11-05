from tokenizing_a_string import Tokenizing
class Infix():
    def infix_to_postfix(self, string):
        postfix_string = ""
        token_list = Tokenizing().tokenize_string(string)
        for char in string:
            if not(char in token_list):
                postfix_string += char
        for token in token_list:
            postfix_string += " " + token
        return postfix_string

if __name__ == '__main__':
    string = raw_input("Enter a string: ")
    print Infix().infix_to_postfix(string)
