# This program calculates the tax, tip, and grand total.

class TaxAndTip():
    LOCAL_TAX = 0.06
    TIP_PERCENT = 0.18
    def tax_and_tip(self, bill):
        tax_owed = bill * self.LOCAL_TAX
        tip_owed = bill * self.TIP_PERCENT
        grand_total = bill + tax_owed + tip_owed
        return "Your tax is %.2f, your tip is %.2f, and your grand total is %.2f."\
        % (tax_owed, tip_owed, grand_total)

bill = float(input("Enter your restaurant bill: "))

calculate = TaxAndTip()
print calculate.tax_and_tip(bill)
