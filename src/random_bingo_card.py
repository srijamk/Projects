import random
class Bingo():
    bingo_card = {
        "B": [],
        "I": [],
        "N": [],
        "G": [],
        "O": []
        }
    ranges = {
    "B": (1, 15),
    "I": (16, 30),
    "N": (31, 45),
    "G": (46, 60),
    "O": (61, 75)
    }
    def get_bingo_card(self):
        card = ["B", "I", "N", "G", "O"]
        random_b = []
        random_i = []
        random_n = []
        random_g = []
        random_o = []
        for x in range(5):
            random_b.append(random.randrange(1, 16))
            random_i.append(random.randrange(16, 31))
            random_n.append(random.randrange(31, 46))
            random_g.append(random.randrange(46, 61))
            random_o.append(random.randrange(61, 75))
        self.bingo_card["B"] = random_b
        self.bingo_card["I"] = random_i
        self.bingo_card["N"] = random_n
        self.bingo_card["G"] = random_g
        self.bingo_card["O"] = random_o
        return self.bingo_card

if __name__ == '__main__':
    print Bingo().get_bingo_card()
