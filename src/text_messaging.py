class TextMessaging():
    letters_dict = {
    1: (".", ",", "?", "!", ":"),
    2: ("a", "b", "c"),
    3: ("d", "e", "f"),
    4: ("g", "h", 'i'),
    5: ("j", "k", "l"),
    6: ("m", "n", "o"),
    7: ("p", "q", "r", "s"),
    8: ("t", "u", "v"),
    9: ("w", "x", "y", "z"),
    0: (" ")

    }
    def get_letters(self, message):
        final_string = ""
        message_letters = []
        for letter in message:
            for key in self.letters_dict:
                if letter in self.letters_dict[key]:
                    message_letters.append(str(key) * (list(self.letters_dict[key]).index(letter) + 1))
        for letter in message_letters:
            final_string += letter
        return final_string

if __name__ == '__main__':
    message = raw_input("Enter a message: ")
    print TextMessaging().get_letters(message)
