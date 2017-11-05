import sys

class Sum():
    def sum_of_consecutive_numbers(self, N):
        sum_nums = 0
        for current_num in range(N + 1):
            sum_nums = sum_nums + current_num
        return sum_nums

if __name__ == '__main__':
    if len(sys.argv) != 2:
        N = raw_input("Please enter a valid number: ")
    else:
        N = sys.argv[1]

    get = Sum()
    print get.sum_of_consecutive_numbers(int(N))
