import sys

class Count():
    def countRange(self, lst, min_value, max_value):
        for element in lst:
            lst[lst.index(element)] = float(lst[lst.index(element)])
        index = 0
        element_counter = 0
        while index < len(lst):
            if min_value <= lst[index] < max_value:
                element_counter += 1
            index += 1
        return element_counter

min_value = int(raw_input("Enter a minimum value: "))
max_value = int(raw_input("Enter a maximum value: "))
number = int(raw_input("Enter a number: "))
number_list = []
if number != "":
    number_list.append(number)
    while number != "":
        number = raw_input("Enter another number: ")
        if number != "":
            number_list.append(number)
        else:
            print Count().countRange(number_list, min_value, max_value)
            sys.exit()
