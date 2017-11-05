import sys

class DragonCurves:
  def dragon_curves(self, n):
    dragon = "F"
    nograd = "F"

    for i in range(n):

      old_dragon = dragon
      dragon = old_dragon + "L" + nograd
      nograd = old_dragon + "R" + nograd
    return dragon

if __name__ == '__main__':
  if len(sys.argv) != 2:
    n = raw_input("Enter one number that represents order N: ").split( )
  else:
    n = sys.argv[1]

  paper = DragonCurves()
  print paper.dragon_curves(int(n))
