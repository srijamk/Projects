import random
import sys

class FairCoin:
  def flip_coin(self):
    if random.random() < 0.5:
      return "Heads"
    else:
      return "Tails"

if __name__ == '__main__':
  coin = FairCoin()
  print coin.flip_coin()
