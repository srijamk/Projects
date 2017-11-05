import random
from avoiding_duplicates import Duplicates
class Lottery():
    def get_lottery_numbers(self):
        number_list = []
        for x in range(6):
            number = random.randint(1, 49)
            while number in number_list:
                number = random.randint(1, 49)
            number_list.append(number)
        return number_list

print Lottery().get_lottery_numbers()
