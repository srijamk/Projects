from leap_year import LeapYear

class DaysInAMonth():
    num_of_days = {
    "January": 31,
    "March": 31,
    "April": 30,
    "May": 31,
    "June": 30,
    "July": 31,
    "August": 31,
    "September": 30,
    "October": 31,
    "November": 30,
    "December": 31
    }
    def get_days(self, month, year):
        if month in self.num_of_days:
            return self.num_of_days[month]
        elif month == "February" and LeapYear().is_leap_year(year):
            return 28
        elif month == "February" and LeapYear().is_leap_year(year) != True:
            return 29
        else:
            return "Invalid date."

GivenMonthAndYear = DaysInAMonth()
month = raw_input("Enter a month: ")
year = int(raw_input("Enter a year: "))
print GivenMonthAndYear.get_days(month, year)
