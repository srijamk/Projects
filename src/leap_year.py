import sys


class LeapYear:
  def is_leap_year(self, year):
    """
    Tests whether an integer corresponds to a leap yearin the Gregorian calendar.
    A year is a leap year if it is divisible by 4(2004), unless it is divisible
    by 100 in which case it is not (1900), unless it is divisible by 400 in which
    case it is (2000).
    """

    leap_year = year % 4 == 0

    leap_year = leap_year and year % 100 != 0

    leap_year = leap_year or year % 400 == 0

    return leap_year


if __name__ == '__main__':

  _leapyear = LeapYear()
  if len(sys.argv) != 2:
    year = raw_input("Enter a valid year: ")
  else:
    year = sys.argv[1]

  print _leapyear.is_leap_year(int(year))
