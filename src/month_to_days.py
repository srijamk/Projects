class MonthtoDays:
    def get_number_of_days(self, month):
        thirty_one = ["JANUARY", "MARCH", "MAY", "JULY", "OCTOBER", "DECEMBER"]
        thirty = ["APRIL", "JUNE", "SEPTEMBER", "NOVEMBER"]
        if (str(month)).upper() in thirty_one:
            return "31 days."
        elif (str(month)).upper() in thirty:
            return "30 days."
        elif (str(month)).upper() == "FEBRUARY":
            return "28 or 29 days."


month = input("Enter month: ")
given_month = MonthtoDays()
print given_month.get_number_of_days(month)
