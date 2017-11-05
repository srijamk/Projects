class Decimal():
    def get_binary(self, n):
        result = ""
        factor = 1
        while factor <= n:
            factor = factor * 2
        while factor > 0:
            if n < factor:
                result += "0"
            else:
                result += "1"
                n -= factor
            factor = factor / 2
        return result[1:]

decimal = int(raw_input("Enter a number: "))
GivenDecimal = Decimal()
print GivenDecimal.get_binary(decimal)
