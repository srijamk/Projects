from random_bingo_card import Bingo
class CheckWin():
    def is_winning_card(self, card):
        is_winner = False
        # All Bs, Is, Ns, Gs, and Os
        if card["B"].count((card["B"])[0]) == 5 or card["I"].count((card["I"])[0]) == 5 or card["N"].count((card["N"])[0]) == 5 or card["G"].count((card["G"])[0]) == 5 or card["O"].count((card["O"])[0]) == 5:
            is_winner = True
        elif card["B"][0] == card["I"][1] == card["N"][2] == card["G"][3] == card["O"][4]:
            is_winner = True
        elif card["B"][4] == card["I"][3] == card["N"][2] == card["G"][1] == card["O"][4]:
            is_winner = True
        elif card["B"][0] == card["I"][0] == card["N"][0] == card["G"][0] == card["O"][0]:
            is_winner = True
        elif card["B"][1] == card["I"][1] == card["N"][1] == card["G"][1] == card["O"][1]:
            is_winner = True
        elif card["B"][2] == card["I"][2] == card["N"][2] == card["G"][2] == card["O"][2]:
            is_winner = True
        elif card["B"][3] == card["I"][3] == card["N"][3] == card["G"][3] == card["O"][3]:
            is_winner = True
        elif card["B"][4] == card["I"][4] == card["N"][4] == card["G"][4] == card["O"][4]:
            is_winner = True

        return is_winner

card = Bingo().get_bingo_card()

if __name__ == '__main__':
    print CheckWin().is_winning_card(card)
