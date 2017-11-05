class Binary():
    def get_decimal(self, num):
        result = 0
        factor = 1
        index = -1
        while index >= 0 - len(num) and factor >= 1:
            if num[index] != "0":
                result += int(num[index]) * factor
            factor = factor * 2
            index -= 1
        return result

num = raw_input("Enter a number in binary: ")
GivenBinary = Binary()
print GivenBinary.get_decimal(num)
