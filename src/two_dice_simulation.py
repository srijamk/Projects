import random

class DiceRolling():
    total_dict = {
    2: 0,
    3: 0,
    4: 0,
    5: 0,
    6: 0,
    7: 0,
    8: 0,
    9: 0,
    10: 0,
    11: 0,
    12: 0
    }
    def simulate_dice(self):
        simulated_percents = []
        expected_percents = []
        for x in range(1001):
            self.total_dict[random.randint(1, 6) + random.randint(1, 6)] += 1

        print "Total    Simulated Percent    Expected Percent"
        for key in self.total_dict:
            print "  " + str(key) + "             " + str(round(float(self.total_dict[key]) / 10.0, 2)) + "                " + str(round(float(self.expected_value(key)), 2))

    def expected_value(self, num):
        counter = 0
        for x in range(1, 7):
            for y in range(1, 7):
                if x + y == num:
                    counter += 1
        return float(counter) / 0.36

print DiceRolling().simulate_dice()
