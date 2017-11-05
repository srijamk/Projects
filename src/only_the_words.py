import re

class OnlyWords():
    def separate_words(self, sentence):
        return filter(None, re.split("[, .\n-!?:]+", sentence))

if __name__ == '__main__':
    string = raw_input("Enter a sentence: ")
    print OnlyWords().separate_words(string)
