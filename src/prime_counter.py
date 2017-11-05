import sys

class PrimeCounter():

  def has_divisors(self, N):
    divisibles = []
    for num in range(1, N):
      if N % num == 0:
        divisibles.append(num)
        if num == 0 or num == 1 or num == N:
          divisibles.remove(num)
    return len(divisibles) > 0

  def get_primes(self, N):
    primes = []
    for num in range(2, N):
      if self.has_divisors(num) == False:
        primes.append(num)
    return "\nThere are " + str(len(primes)) + " primes.\n"

if __name__ == '__main__':
  if len(sys.argv) != 2:
    N = raw_input("Enter one number: ").split( )
  else:
    N = sys.argv[1]

  number = PrimeCounter()
  print number.get_primes(int(N))
