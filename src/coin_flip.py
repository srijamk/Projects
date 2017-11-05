import random
class Coin():
    average_flips = []
    def get_flips(self):
        result = ""
        flip_counter = 0
        while 'H H H' not in result and 'T T T' not in result:
            random_flip = random.randint(1, 2)
            flip_counter += 1
            if random_flip == 1:
                result += "H "
            else:
                result += "T "
        self.average_flips.append(flip_counter)
        return result + "(%i flips)" % flip_counter

    def get_average(self):
        return "On average, %.1f flips were needed. " % (float(sum(self.average_flips)) / float(len(self.average_flips)))
        #return "On average, %i flips were needed. " % (sum(average_flips) / len(average_flips))
GivenCoin = Coin()
print
for x in range(10):
    print GivenCoin.get_flips()
print GivenCoin.get_average()
print
