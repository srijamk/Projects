class Gcd():
    def get_gcd(self, m, n):
        # m / 2 is the greatest factor of m other than m.
        # If 
        if max(m, n) % min(m, n) != 0:
            d = min(m, n) / 2
            while m % d != 0 or n % d != 0:
                d -= 1
        else:
            d = min(m, n)
        return d


m = int(raw_input("Enter a number: "))
n = int(raw_input("Enter a number: "))
GivenNumbers = Gcd()
print GivenNumbers.get_gcd(m, n)
