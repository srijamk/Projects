import math
import random

# Z = sin(2 pi v)*(-2 ln(u) )^1/2

def std_gaussian():
    u = random.random()
    v = random.random()
    return (math.sin(2 * math.pi * v)) * (math.pow(-2 * math.log(u), 0.5))

print std_gaussian()
