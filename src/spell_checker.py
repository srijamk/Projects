from only_the_words import OnlyWords
import re

class Spelling():
    english_words = {

    }
    def get_miswords(self, text_file):
        words_in_file = set()
        sentence = ''
        with open(text_file, 'r') as f:
            all_text = f.read()
            # Filters the invalid characters out
            distinct_alphanumeric = set(filter(None, re.split("[, .\n-!?:]+", all_text)))
            distinct_words = set()
            for word in distinct_alphanumeric:
                if not word.isdigit():
                    # Alphanumeric set includes numbers, this list filters out numbers
                    distinct_words.add(word)
        with open('english_dictionary.txt', 'r') as e:
            all_words = e.read()
            for word in distinct_words:
                if word.lower() not in all_words:
                    print word

print Spelling().get_miswords('new_file.py')
