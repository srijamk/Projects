class Scrabble():
    scrabble_dict = {
    ("A", "E", "I", "L", "N", "O", "R", "S", "T", "U"): 1,
    ("D", "G"): 2,
    ("B", "C", "M", "P"): 3,
    ("F", "H", "V", "W", "Y"): 4,
    ("K"): 5,
    ("J", "X"): 8,
    ("Q", "Z"): 10
    }
    def get_scrabble_score(self, word):
        score = 0
        for char in word:
            for letters in self.scrabble_dict:
                if char in letters:
                    score += self.scrabble_dict[letters]
        return str(score)

    def main(self):
        # Should return 8, 8
        return self.get_scrabble_score("HELLO") + "\n" + self.get_scrabble_score("BEETLE")

print Scrabble().main()
