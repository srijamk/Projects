class UnitsOfTime():
    SECONDS_IN_DAYS = 86400
    SECONDS_IN_HOUR = 3600
    SECONDS_IN_MINUTE = 60

    def zero_formatter(self, variable):
        if int(variable) < 10:
            variable = "0" + str(variable)

        return variable

    def get_units_of_time(self, seconds):
        days = str(seconds / self.SECONDS_IN_DAYS)
        hours = str(seconds % self.SECONDS_IN_DAYS / self.SECONDS_IN_HOUR)
        minutes = str(seconds % self.SECONDS_IN_DAYS % self.SECONDS_IN_HOUR / self.SECONDS_IN_MINUTE)
        seconds = seconds % self.SECONDS_IN_DAYS % self.SECONDS_IN_HOUR % self.SECONDS_IN_MINUTE

        return "%s:%s:%s:%s" % (days, self.zero_formatter(hours), self.zero_formatter(minutes), self.zero_formatter(seconds))

seconds = int(input("Enter the number of seconds: "))
measurements = UnitsOfTime()
print measurements.get_units_of_time(seconds)
