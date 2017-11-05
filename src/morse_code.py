class Morse():
    morse_dict = {
    "A": ".- ",
    "B": "-... ",
    "C": "-.-. ",
    "D": "-.. ",
    "E": ". ",
    "F": "..-. ",
    "G": "--. ",
    "H": ".... ",
    "I": ".. ",
    "J": ".--- ",
    "K": "-.- ",
    "L": ".-.. ",
    "M": "-- ",
    "N": "-. ",
    "O": "--- ",
    "P": ".--. ",
    "Q": "--.- ",
    "R": ".-. ",
    "S": "... ",
    "T": "- ",
    "U": "..- ",
    "V": "...- ",
    "W": ".-- ",
    "X": "-..- ",
    "Y": "-.-- ",
    "Z": "--.. ",
    "1": ".---- ",
    "2": "..--- ",
    "3": "...-- ",
    "4": "....- ",
    "5": "..... ",
    "6": "-.... ",
    "7": "--... ",
    "8": "---.. ",
    "9": "----. "
    }
    def get_morse_code(self, message):
        morse_str = ""
        for char in message:
            if char.upper() in self.morse_dict and 65 <= ord(char.upper()) <= 90:
                morse_str += self.morse_dict[char.upper()]
            if char in self.morse_dict and not(65 <= ord(char) <= 90):
                morse_str += self.morse_dict[char]
        return morse_str

    def main(self):
        # Should return:
        # .... . .-.. .-.. --- .-- --- .-. .-.. -..
        return self.get_morse_code("Hello World!")

print Morse().main()
