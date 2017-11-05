class Pi():
    def get_digits(self):
        a = 2.0
        b = a + 1.0
        c = a + 2.0
        return_value = 3
        for i in range(10000):
            if i % 2 == 0:  
                return_value += 4.0 / (a * b * c)
            else:
                return_value -= 4.0 / (a * b * c)
            print return_value
            a += 2
            b += 2
            c += 2
GivenSequence = Pi()
print GivenSequence.get_digits()
