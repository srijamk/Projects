class NumberToLetter():
    ones_place = {
    0: "",
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine"
    }
    hundreds_place = {
    1: "one hundred ",
    2: "two hundred ",
    3: "three hundred ",
    4: "four hundred ",
    5: "five hundred ",
    6: "six hundred ",
    7: "seven hundred ",
    8: "eight hundred ",
    9: "nine hundred "
    }

    tens_place = {
    0: "",
    2: "twenty ",
    3: "thirty ",
    4: "forty ",
    5: "fifty ",
    6: "sixty ",
    7: "seventy ",
    8: "eighty ",
    9: "ninety "
    }
    ten_to_nineteen = {
    10: "ten",
    11: "eleven",
    12: "twelve",
    13: "thirteen",
    14: "fourteen",
    15: "fifteen",
    16: "sixteen",
    17: "seventeen",
    18: "eighteen",
    19: "nineteen"
    }

    def get_english(self, number):
        number = str(number)
        if len(number) == 3 and number[1] != "1":
            return self.hundreds_place[int(number[0])] + self.tens_place[int(number[1])] + self.ones_place[int(number[2])]
        elif len(number) == 3 and number[1] == "1":
            return self.hundreds_place[int(number[0])] + self.ten_to_nineteen[int(number[1:])]
        if len(number) == 2 and number[0] != "1":
            return self.tens_place[int(number[0])] + self.ones_place[int(number[1])]
        elif len(number) == 2 and number[0] == "1":
            return self.ten_to_nineteen[int(number)]
        else:
            return int(number)
    def main(self):
        # Should return nine hundred eighty one
        return self.get_english(981)

print NumberToLetter().main()
