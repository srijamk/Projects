class ReduceFraction():
    def get_greatest_common_divisor(self, numerator, denominator):
        common_factor_list = []
        factor = 1
        while factor <= numerator:
            if numerator % factor == 0 and denominator % factor == 0:
                common_factor_list.append(factor)
            factor += 1
        return "Reduced fraction is %i/%i" % (numerator / (factor - 1), denominator / (factor - 1))

numerator = int(raw_input("Enter the numerator: "))
denominator = int(raw_input("Enter the denominator: "))
GivenFraction = ReduceFraction()
print GivenFraction.get_greatest_common_divisor(numerator, denominator)
