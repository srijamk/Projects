import unittest
from loan_payment import LoanPayment

class TestLoanPayment(unittest.TestCase):
  def test_monthly_payment(self):
    loan = LoanPayment()
    self.assertEqual(2.72, loan.monthly_payment(1, 1, 1))
    self.assertEqual(5.44, loan.monthly_payment(1, 2, 1))

if __name__ == '__main__':
  unittest.main()
