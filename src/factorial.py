# 5! = 5 * 4 * 3 * 2 * 1

# n! = n * (n-1)!

def factorial (n):

  if n <= 0:
    print "n must be greater than 0"

  if n == 1:
    return 1

  return n * factorial (n - 1)



print factorial (5)
