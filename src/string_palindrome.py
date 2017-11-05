class Palindrome():
    invalid_characters = [" ", ".", "?", "!", ":", "-"]
    def get_palindrome(self, string):
        # check whether the string's start and end characters are equal
        # if so, continue to next set of characters
        for character in self.invalid_characters:
            if character in string:
                string.replace(character, "")
        string = string.lower()
        start_index = 0
        end_index = len(string) - 1
        for x in range(len(string) / 2):
            return string[start_index] == string[end_index]

string = raw_input("Enter a string: ")
GivenString = Palindrome()
print GivenString.get_palindrome(string)
