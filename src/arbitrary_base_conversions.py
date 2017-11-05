class Convert():
    def get_base(self, original_base, num):
        result = 0
        for index in range(len(num)):
            result += num[index] * (6 ** index)
        return result

    def get_decimal(self, return_base, num):
        result = ""
        remainder_list = []

        while num > 0:
            quotient = num / return_base
            remainder = num - (quotient * return_base)
            remainder_list.append(str(remainder))
            num = num / return_base

        for item in list(reversed(remainder_list)):
            result += item
        return result


original_base = int(raw_input("Enter a base: "))
num = int(raw_input("Enter a number in the original base: "))
return_base = int(raw_input("Enter a base: "))
print Convert().get_decimal(original_base, num)
