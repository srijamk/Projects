def credit_card(balance, annualInterestRate, monthlyPaymentRate):
    new_balance = balance
    minimum_payment = new_balance * monthlyPaymentRate
    total_payment = 0
    monthly_interest_rate = annualInterestRate / 12.0
    for month in range(1, 13):
        print "Month: " + str(month)
        print "Minimum Monthly Payment: " + str(round(new_balance * monthlyPaymentRate, 2))
        print "Remaining balance: " + str(round(new_balance - minimum_payment + (monthly_interest_rate * (new_balance - minimum_payment)), 2))
        print
        total_payment += minimum_payment
        new_balance = new_balance - minimum_payment + (monthly_interest_rate * (new_balance - minimum_payment))
        minimum_payment = new_balance * monthlyPaymentRate
        print minimum_payment + (monthly_interest_rate * (new_balance - minimum_payment))
    print "Total paid: " + str(round(total_payment, 2))
    print "Remaining balance: " + str(round(new_balance, 2))
credit_card(4213, 0.2, 0.04)
