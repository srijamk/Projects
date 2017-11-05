import sys
import random
import time

class MeasureTime():
  def measure(self, trials, n, alg):
    total_time = 0
    for x in range(0, trials):
      random_nums = []
      for y in range(0, n):
        random_nums.append(random.randrange(n+1))

      start = time.time()
      alg.sort(random_nums)
      end = time.time()
      elapsed_time = end - start
      print elapsed_time
      total_time += elapsed_time
    avg_time = total_time / trials
    return avg_time
