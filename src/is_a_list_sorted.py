import sys

class Sorted():
    def is_sorted(self, lst):
        is_sorted = True
        if len(lst) == 0:
            return is_sorted
        index = 0
        is_ascending = lst[0] < lst[-1]
        for index in range(0, len(lst) - 1):
            if is_ascending and not(lst[index] <= lst[index + 1]):
                is_sorted = False
                break
            elif not(is_ascending) and not(lst[index] >= lst[index + 1]):
                is_sorted = False
                break

            index += 1
        return is_sorted

number = raw_input("Enter to continue. ")
is_space = False
lst = []
if number == "":
    while number != " ":
        number = raw_input("Enter a number: ")
        if number != "":
            lst.append(int(number))
        else:
            print Sorted().is_sorted(lst)
            sys.exit()
