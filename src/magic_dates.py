from test_leap_year import LeapYear
class MagicDates():
    num_of_days = {
    1: 31,
    2: 28,
    3: 31,
    4: 30,
    5: 31,
    6: 30,
    7: 31,
    8: 31,
    9: 30,
    10: 31,
    11: 30,
    12: 31
    }
    def get_magic_dates(self):
        month = 0
        while month <= 11:
            for year in range(1900, 2000): # year
                # day # month
                specified_month = self.num_of_days.keys()[month]
                specified_year = str(year)
                for date in range(1, self.num_of_days.values()[month] + 1):
                    if specified_month * int(date) == int(specified_year[2:]):
                        print str(specified_month), str(date), specified_year
            month += 1


GivenDate = MagicDates()
print GivenDate.get_magic_dates()
