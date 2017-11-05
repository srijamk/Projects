class TextMessages():
    CALL_CENTER_CHARGE = 0.44
    SALES_TAX = 0.05
    def get_charge(self, minutes, messages):
        if minutes + messages <= 100:
            return SALES_TAX * (15.00 + CALL_CENTER_CHARGE)
