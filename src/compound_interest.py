class CompoundInterest():
    INTEREST_RATE = 0.04
    def compound_interest(self, initial_balance):
        one_year = initial_balance + initial_balance * 0.04
        two_years = one_year * 1.04
        three_years = two_years * 1.04

        return "In one year, the balance will be %.2f, in two years the balance"\
        " will be %.2f, and in the three years the balance will be %.2f."\
        % (one_year, two_years, three_years)

initial_balance = int(input("Enter your initial balance: "))
calculate = CompoundInterest()
print calculate.compound_interest(initial_balance)
