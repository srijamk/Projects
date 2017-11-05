
import string
class Letters():
    def get_letter_frequencies(self, file_name):
        letters = []
        invalid_chars = ["!", "?", ".", "1", "2", "3", "4", "5", "6", "7", "8", "9", " ", ";", ":", "-", ","]
        with open(file_name,'r') as f:
            for line in f:
                for letter in line:
                    letters.append(letter)

        for index, letter in enumerate(letters):
            if letter in list(string.ascii_uppercase):
                letters[index] = letter.upper()

        for letter in list(string.ascii_lowercase):
            print str(letter.upper()) + ": " + str(letters.count(letter))

print Letters().get_letter_frequencies('Carbs.rtf')
