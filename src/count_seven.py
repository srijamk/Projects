def count7(N):
    '''
    N: a non-negative integer
    '''
    counter = 0
    if N == 0:
         return counter 
    if N % 10 == 7:
        counter += 1
    N = N / 10
    counter += count7(N)
    return counter

print count7(1237123)
print count7(8989)
        

    
