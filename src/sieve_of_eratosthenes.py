import time
import math
class Eratosthenes():
    def sieve_of_eratosthenes(self, n):
        numbers = []
        for x in range(n + 1):
            numbers.append(True)
        for x in range(2, n + 1):
            if numbers[x] == True:
                for number in range(x, n / x + 1):
                    numbers[number * x] = False

        for index, item in enumerate(numbers[2:]):
            if item == True:
                print index + 2

    def all_primes(self, n):
        for i in range(2, n + 1):
            is_prime = True
            for j in range(2, int(math.sqrt(i - 1))):
                if i % j == 0:
                    is_prime = False
                    break
            if is_prime:
                print i

n = int(raw_input("Enter a number: "))
start = time.time()
#print Eratosthenes().all_prime_numbers(n)
#print Eratosthenes().all_primes(n)
print Eratosthenes().sieve_of_eratosthenes(n)
end = time.time()
print end - start
