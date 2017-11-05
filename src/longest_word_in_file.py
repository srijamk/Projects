class Word():
    def get_longest_word(self, file):
        f_words = []
        with open(file,'r') as f:
            for line in f:
                for word in line.split():
                    f_words.append(len(word))
        longest_length = max(f_words)
        with open(file, 'r') as f:
            for line in f:
                for word in line.split():
                    if len(word) == longest_length:
                        print word
        return "Length of word(s): %i" % longest_length

print Word().get_longest_word("ord_to_letter.py")
