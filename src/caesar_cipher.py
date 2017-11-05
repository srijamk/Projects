
import string
class Caesar():
    final_message = ""
    def get_message(self, message, shift_amount):
        for letter in message:
            letter = letter.lower()
            # string.letters is a collection of letters from a-z and A-Z
            # if the character is a valid letter, change the letter's position to where it should be
            if letter in string.letters:
                letter = string.letters[string.letters.index(letter) + int(shift_amount)]
            # if a changed letter is not valid (ex: Z with shift amount 1 does not have an index to go on to)
            # make the Z a z so the position will go on to A
            self.final_message += letter
        return self.final_message

message = raw_input("Enter your message! ")
shift_amount = raw_input("Enter the shift amount! ")
GivenMessage = Caesar()
print GivenMessage.get_message(message, shift_amount)
