import random
from check_bingo_win import CheckWin
from random_bingo_card import Bingo
class Play():
    letter_to_ranges = {
    "B": (1, 16),
    "I": (16, 31),
    "N": (31, 46),
    "G": (46, 61),
    "O": (61, 76)
    }

    def play_bingo(self):
        # Creates list of valid bingo calls (ex: B5, G51)
        number_of_calls = []
        for x in range(1, 1001):
            counter = 0
            random_card = Bingo().get_bingo_card()
            valid_bingo_calls = ['B1', 'B2', 'B3', 'B4', 'B5', 'B6', 'B7', 'B8', 'B9', 'B10', 'B11', 'B12', 'B13', 'B14', 'B15', 'I16', 'I17', 'I18', 'I19', 'I20', 'I21', 'I22', 'I23', 'I24', 'I25', 'I26', 'I27', 'I28', 'I29', 'I30', 'N31', 'N32', 'N33', 'N34', 'N35', 'N36', 'N37', 'N38', 'N39', 'N40', 'N41', 'N42', 'N43', 'N44', 'N45', 'G46', 'G47', 'G48', 'G49', 'G50', 'G51', 'G52', 'G53', 'G54', 'G55', 'G56', 'G57', 'G58', 'G59', 'G60', 'O61', 'O62', 'O63', 'O64', 'O65', 'O66', 'O67', 'O68', 'O69', 'O70', 'O71', 'O72', 'O73', 'O74', 'O75']
            random.shuffle(valid_bingo_calls)
            while CheckWin().is_winning_card(random_card) == False:
                for value in random_card.values():
                    if int(valid_bingo_calls[0][1:]) in value:
                        value[value.index(int(valid_bingo_calls[0][1:]))] = 0
                counter += 1
                valid_bingo_calls.pop(0)

            if CheckWin().is_winning_card(random_card):
                number_of_calls.append(counter)

        return "Minimum Number of Calls: %i\nMaximum Number of Calls: %i\nAverage Number of Calls: %i " % (min(number_of_calls), max(number_of_calls), (sum(number_of_calls) / 1000))
    def get_key(self, dictionary, value):
        for key in dictionary:
            if dictionary[key] == value:
                return key

print Play().play_bingo()
