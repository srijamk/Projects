import re

class Words():
    def get_repeated_words(self, file_name):
        text = []

        # Breaks text into separate words
        with open(file_name, 'r') as f:
            for line in f.readlines():
                line = filter(None, re.split("[, .\n-!?:]+", line))
                text.append(line)

        # Prints word if it is repeated between lists

        index = 0
        while index < len(text) - 1:
            if text[index][-1] == text[index + 1][0]:
                print "The word '%s' is repeated on lines %i and %i." % (text[index][-1], index + 1, index + 2)
            index += 1

        # Prints word if it is repeated within lists

        for sentence in text:
            index = 0
            while index < len(sentence) - 1:
                if sentence[index] == sentence[index + 1]:
                    print "The word '%s' is repeated on line %i." % (sentence[index], text.index(sentence) + 1)
                index += 1

print Words().get_repeated_words('new_file.py')
