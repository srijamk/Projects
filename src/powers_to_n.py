import sys
import math
import random

class Loops():
    def powers_of_two(self, N):
        for x in range(N):
            print 2**x

    def largest_power_of_two_less_than_equal_to_N(self, N):
        result = 1
        while result <= N / 2:
            result = result * 2
            print result

    def sum_of_consecutive_numbers(self, N):

        sum_nums = 0
        for current_num in range(N + 1):
            sum_nums = sum_nums + current_num
        return sum_nums

    def product_of_consecutive_numbers(self, N):
        sum_nums = 1
        for current_num in range(1, N + 1):
            sum_nums = sum_nums * current_num
        return sum_nums

    def list_of_random_numbers(self, N):
        random_nums = []
        y = random.randint(1, 100)
        for x in range(N):
            random_nums.append(y)
            return random_nums, max(random_nums), min(random_nums)


if __name__ == '__main__':
    if len(sys.argv) != 2:
        N = raw_input("Please type a valid number: ")
    else:
        N = sys.argv[1]

    get_powers = Loops()
    print get_powers.list_of_random_numbers(int(N))
