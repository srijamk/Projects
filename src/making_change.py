class MakingChange():
    DOLLAR = 100
    QUARTER = 25
    DIME = 10
    NICKEL = 5
    def remainder(self, divisor, dividend):
        quotient = divisor / dividend
        remainder = divisor % dividend

        return quotient, remainder
    def get_change(self, cash):
        dollars, cash = self.remainder(cash, self.DOLLAR)
        quarters, cash = self.remainder(cash, self.QUARTER)
        dimes, cash = self.remainder(cash, self.DIME)
        nickels, cash = self.remainder(cash, self.NICKEL)
        return "%d dollars, %d quarters, %d dimes, %d nickels, and %d pennies." \
        % (dollars, quarters, dimes, nickels, cash)

cash = int(input("Enter your cash here: "))
purchase = MakingChange()
print purchase.get_change(cash)
