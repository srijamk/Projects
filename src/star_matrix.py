import sys

class StarMatrix():
  def star_matrix(self, N):
    if N == 1:
      return N * "*"
    else:
      i = 0
      j = 0
      stars = ""
      for i in range(N):
        for j in range(N):
          stars += "*"
        stars += "\n"
    return stars



if __name__ == '__main__':
  if len(sys.argv) != 2:
    N = raw_input("Enter one number: ")
  else:
    N = sys.argv[1]

  number = StarMatrix()
  print number.star_matrix(int(N))
