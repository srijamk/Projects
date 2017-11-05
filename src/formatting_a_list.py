class Formatting():
    def format_list(self, lst):
        format_string = ""
        if len(lst) == 1:
            return lst[0]
        elif len(lst) == 2:
            return lst[0] + " and " + lst[1]
        else:
            for item in lst[0:-1]:
                format_string += item + ", "
            format_string += "and " + lst[-1]
        return format_string

first_word = raw_input("Press Enter to continue: ")
word_list = []
if first_word == "":
    while first_word != "0":
        if first_word != "0":
            first_word = raw_input("Enter a word: ")
            word_list.append(first_word)
print Formatting().format_list(word_list[0:-1   ])
