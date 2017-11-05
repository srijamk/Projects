from is_prime import IsPrime

def get_10001th_prime():
    prime_counter = 0
    num = 2
    while prime_counter < 10001:
        if IsPrime().is_prime(num):
            prime_counter += 1
        num += 1
    return num - 1

print get_10001th_prime()

# Result: 104743
