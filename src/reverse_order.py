class Reversed():
    def get_reverse_order(self, lst):
        return list(reversed(lst))

number = raw_input("Press Enter to continue: ")
number_list = []
if number == "":
    while number != 0:
        number = int(raw_input("Enter a number: "))
        if number != 0:
            number_list.append(number)
        else:
            print Reversed().get_reverse_order(number_list)
