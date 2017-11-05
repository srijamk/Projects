class SortedOrder():
    def get_sorted_order(self, lst):
        return sorted(lst)

number = raw_input("Press Enter to continue. ")
number_list = []
if number == "":
    while number != 0:
        number = int(raw_input("Enter a number: "))
        if number == 0:
            print SortedOrder().get_sorted_order(number_list)
        else:
            number_list.append(number)
