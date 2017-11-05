import random

class Maximum():
    MAX_VALUE = 100
    def get_max_value(self):
        num_updates = 0
        max_value = random.randint(1, self.MAX_VALUE)
        additional_value = random.randint(1, self.MAX_VALUE)
        random_values = [max_value, additional_value]
        while len(random_values) <= self.MAX_VALUE:
            random_values.append(random.randint(1, self.MAX_VALUE))

        for current in random_values:
            if current > max_value:
                num_updates += 1
                max_value = current
                current = str(max_value) + " <== Update"
            print current
        print "Maximum Value is " + str(max_value)
        print "Maximum Value was found " + str(num_updates) + " times."


GivenRandom = Maximum()
print GivenRandom.get_max_value()
