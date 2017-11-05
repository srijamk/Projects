import math
class Quadratic():
  def solve(self, b, c):
    discriminant = math.sqrt(b ** 2 - (4 * c))
    root1 = -(b + discriminant) / 2
    root2 = (- b + discriminant) / 2
    return tuple((root1, root2))

_quadratic = Quadratic()
print _quadratic.solve(3, 2)
