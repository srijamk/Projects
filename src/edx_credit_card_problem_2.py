def credit_card(balance, annualInterestRate):
    new_balance = balance
    monthly_interest_rate = annualInterestRate / 12.0
    # Lower bound represents equal monthly installments
    lower_bound = balance / 12
    # Upper bound represents monthly installments plus interest
    upper_bound = (balance * (1 + monthly_interest_rate) ** 12) / 12.0
    monthly_payment = lower_bound
    print lower_bound, upper_bound

    while True:
        new_balance = balance
        monthly_payment = (lower_bound + upper_bound) / 2
        month = 1
        # Program compounds full year
        while month <= 12:
            new_balance -= monthly_payment
            new_balance += (new_balance * monthly_interest_rate)
            month += 1

        # If new_balance is within a cent of zero, return the monthly payment
        if -0.01 < new_balance < 0.01:
            break
        elif new_balance > 0.01:
            lower_bound = monthly_payment
        elif new_balance < 0.01:
            upper_bound = monthly_payment

    print monthly_payment


print credit_card(999999, 0.18)
