import sys

class FacesOnMoney():
    bank_notes = {"1": "George Washington", "2":"Thomas Jefferson", \
    "5":"Abraham Lincoln", "10":"Alexander Hamilton", "20":"Andrew Jackson", \
    "50":"Ulysses S. Grant", "100":"Benjamin Franklin"}

    def validate_amount(self, amount):
        return amount in self.bank_notes.keys()

    def get_face(self, amount):
        return self.bank_notes[amount]

amount = raw_input("Enter an amount: ")
given_amount = FacesOnMoney()
while given_amount.validate_amount(amount) == False:
    amount = raw_input("Please enter a valid amount. Press enter to Exit: ")
    if amount == "":
        print "Exited."
        sys.exit()
print given_amount.get_face(amount)
