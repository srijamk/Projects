import sys

class HarmonicNumbers:
  def harmonic_numbers(self, N):
    num_sum = 1.0
    for x in range(2, N + 1):
      result = round(1.0 / float(x), 2)
      num_sum += result
    return num_sum

if __name__ == '__main__':
  if len(sys.argv) != 2:
    num = raw_input("Please enter one number: ")
  else:
    num = sys.argv[1]
  N = HarmonicNumbers()
  print N.harmonic_numbers(int(num))
