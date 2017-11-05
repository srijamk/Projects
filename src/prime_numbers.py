def primesList(N):
    '''
    N: an integer
    '''
    primes_list = []
    for num in range(2, N + 1):
        is_prime = True
        for x in range(2, num / 2 + 1):
             if num % x == 0:
                 is_prime = False
        if is_prime == True:
            primes_list.append(num)
    return primes_list

