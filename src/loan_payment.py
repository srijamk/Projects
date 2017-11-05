import sys
import math

class LoanPayment:
  def monthly_payment(self, t, p, r):
    return round(p * math.exp(r * t), 2)

if __name__ == '__main__':
  print sys.argv[0]
  if len(sys.argv) != 4:
    time, principal, rate = raw_input("Enter 3 values in the respective order - Time(Years), Principal, Rate: ").split( )

  else:
    time = sys.argv[1]
    principal = sys.argv[2]
    rate = sys.argv[3]

  loan = LoanPayment()
  print loan.monthly_payment(int(time), int(principal), int(rate))
