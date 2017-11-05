class Words():
    def get_words(self, file_name):
        invalid_chars = ["!", "?", ".", "1", "2", "3", "4", "5", "6", "7", "8", "9", " ", ";", ":", "-", ","]
        word_count = []
        word_list = []
        frequent_word_list = []
        with open(file_name,'r') as f:
            for line in f:
                for word in line.split():
                    word_list.append(str(word))

        for index, word in enumerate(word_list):
            for char in word:
                if char in invalid_chars:
                    word_list[index] = word_list[index].strip(char)
            word_list[index] = word_list[index].lower()

        for word in word_list:
            word_count.append(word_list.count(word))
            if word_list.count(word) == max(word_count):
                frequent_word_list.append(word)

        return list(set(frequent_word_list))
print Words().get_words('new_file.py')
