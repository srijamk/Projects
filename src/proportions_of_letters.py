import string
class Letter():
    def get_proportions(self, file_name):
        letter_list = []
        letter_count = []
        with open(file_name, 'r') as f:
            for line in f:
                for word in line.split():
                    for letter in word:
                        letter_list.append(letter.lower())

        for letter in list(string.lowercase):
            letter_count.append(float(letter_list.count(letter) / float(len(letter_list))))
            print str(letter.upper()) + ": " + "%.2f" % float(letter_list.count(letter) / float(len(letter_list)))

        print "Least Used Letter(s):"
        for letter in list(string.lowercase):
            if round(float(letter_list.count(letter) / float(len(letter_list))), 2) == min(letter_count):
                print str(letter)

print Letter().get_proportions('new_file.py')
