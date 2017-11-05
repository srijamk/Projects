import sys

class LeapYear():
    def get_year(self, year):
        if year % 400 == 0 or (year % 400 != 0 and year % 4 == 0):
            return True
        else:
            return False

if __name__ == '__main__':
    if len(sys.argv) != 2:
        year = int(raw_input("Enter a year: "))
    GivenYear = LeapYear()
    print GivenYear.get_year(year)
