import random

class Password():
    def get_password(self, file_name):
        word_list = []
        second_choice_list = []
        with open(file_name, 'r') as f:
            for line in f:
                for word in line.split():
                    word_list.append(word)

        for index, word in enumerate(word_list):
            if len(word) < 3:
                word_list.pop(index)

        random_first_word = random.choice(word_list)
        for word in word_list:
            if len(word) <= 10 - len(random_first_word):
                second_choice_list.append(word)

        return random_first_word + random.choice(second_choice_list)

print Password().get_password('new_file.py')
