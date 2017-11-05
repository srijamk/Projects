class Bakery():
    REGULAR_PRICE = 3.49
    DISCOUNT_PRICE = 3.49 * 0.6
    FULL_PRICE = 3.49 * 0.4
    def get_price(self, loaves):
        return "The regular price is %.2f, the discount is %.2f, and the grand total is %.2f." \
        % (self.REGULAR_PRICE * loaves, self.DISCOUNT_PRICE * \
        loaves, self.FULL_PRICE * loaves)

amount_of_loaves = int(input("Enter the amount of loaves: "))
measurements = Bakery()
print measurements.get_price(amount_of_loaves)
