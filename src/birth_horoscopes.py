months = {
"1": "January",
"2": "February",
"3": "March",
"4": "April",
"5": "May",
"6": "June",
"7": "July",
"8": "August",
"9": "September",
"10": "October",
"11": "November",
"12": "December"
}

class BirthToHoroscope():

    zodiac_signs = {
    "Capricorn": (("December", 22), ("January", 19)),
    "Aquarius": (("January", 20), ("February", 18)),
    "Pisces": (("February", 19), ("March", 20)),
    "Aries": (("March", 18), ("April", 19)),
    "Taurus": (("April", 20), ("May", 20)),
    "Gemini": (("May", 21), ("June", 20)),
    "Cancer": (("June", 21), ("July", 22)),
    "Leo": (("July", 23), ("August", 22)),
    "Virgo": (("August", 23), ("September", 22)),
    "Libra": (("September", 23), ("October", 22)),
    "Scorpio": (("October", 23), ("November", 21)),
    "Sagittarius": (("November", 22), ("December", 21))

    }

    def in_range(self, monthdayRange, month, day):
        if monthdayRange[0][0] == month:
            return monthdayRange[0][1] <= day
        elif monthdayRange[1][0] == month:
            return monthdayRange[1][1] >= day
        else:
            return False

    def get_zodiac_sign(self, month, day):

        for key in self.zodiac_signs.keys():
            if self.in_range(self.zodiac_signs[key], month, day):
                return "Your zodiac sign is.... %s." % key


month = str(raw_input("Enter your birth month: "))
day = str(raw_input("Enter your birthday: "))
givenMonthAndDay = BirthToHoroscope()
if month in months.keys():
    month = months[month]
print givenMonthAndDay.get_zodiac_sign(month, int(day))
