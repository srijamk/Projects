def largest_prime_factor(num):
    prime_list = []
    factor = 2
    while factor <= num:
        if num % factor == 0:
            prime_list.append(factor)
            # Formerly the program decreased the value of factor
            # But it should have instead decreased the value of n
            num = num // factor
        else:
            factor += 1
    return max(prime_list)

print largest_prime_factor(600851475143)

# Answer: 6,857
