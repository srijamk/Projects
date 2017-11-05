import sys

class StarsAndNumbers():
  def stars_and_numbers(self, N):
    if N == 1:
      return N * "*"
    else:

      stars = ""
      for row in range(1, N + 1):
        for col in range(1, N + 1):
          if row % col == 0 or col % row == 0:
            stars += "*"
          else:
            stars += " "
        stars += "\n"
    return stars

if __name__ == '__main__':
  if len(sys.argv) != 2:
    N = raw_input("Enter one number: ")
  else:
    N = sys.argv[1]

  number = StarsAndNumbers()
  print number.stars_and_numbers(int(N))
