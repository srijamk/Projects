class Prime():
    def get_prime_factors(self, n):
        prime_list = []
        factor = 2
        while factor <= n:
            if n % factor == 0:
                prime_list.append(factor)
                # Formerly the program decreased the value of factor
                # But it should have instead decreased the value of n
                n = n // factor
            else:
                factor += 1
        return prime_list

number = int(raw_input("Enter a number: "))
GivenNumber = Prime()
prime_list = GivenNumber.get_prime_factors(number)
for prime in prime_list:
    print prime
