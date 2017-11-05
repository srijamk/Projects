class ProperDivisors():
    def get_proper_divisors(self, number):
        proper_divisors_list = []
        for x in range(1, number):
            if number % x == 0:
                proper_divisors_list.append(x)
        return proper_divisors_list

if __name__ == '__main__':
    if len(sys.argv) != 2:
        number = int(raw_input("Enter a number: "))
        print ProperDivisors().get_proper_divisors(number)
