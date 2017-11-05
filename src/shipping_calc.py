class Shipping():
    FIRST_ITEM_COST = 10.95
    SUBSEQUENT_ITEM_COST = 2.95
    def get_rate(self, num_of_items):
        if num_of_items > 0:
            return "Cost is $%.2f. " % (self.FIRST_ITEM_COST + ((num_of_items - 1) * self.SUBSEQUENT_ITEM_COST))
        else:
            return "Cost is $0."
num_of_items = int(raw_input("Enter a number of items: "))
GivenNumOfItems = Shipping()
print GivenNumOfItems.get_rate(num_of_items)
