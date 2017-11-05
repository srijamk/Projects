class NextLeapYear():
    def get_year(self, year):
        return year % 400 == 0 or (year % 400 != 0 and year % 4 == 0)

        
