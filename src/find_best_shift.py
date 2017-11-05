import string

def buildCoder(shift):
     """
     Returns a dict that can apply a Caesar cipher to a letter.
     The cipher is defined by the shift value. Ignores non-letter characters
     like punctuation, numbers, and spaces.
 
     shift: 0 <= int < 26
     returns: dict
     """
     caesar_dict = {}
     upper_letters = string.ascii_uppercase
     lower_letters = string.ascii_lowercase
     for letter in upper_letters:
         if not (ord(letter) + shift > 90):
             caesar_dict[letter] = chr(ord(letter) + shift)
         else:
             caesar_dict[letter] = chr(((ord(letter) + shift) - 91) + 65)
     for letter in lower_letters:
         if not (ord(letter) + shift > 122):
             caesar_dict[letter] = chr(ord(letter) + shift)
         else:
             caesar_dict[letter] = chr(((ord(letter) + shift) - 123) + 97)
     return caesar_dict


def applyCoder(text, coder):
    index = 0
    result = ''
    while index < len(text):
        try:
            result += (coder[text[index]])
        except:
            result += (text[index])
        index += 1
    return result


def applyShift(text, shift):
    """
    Given a text, returns a new text Caesar shifted by the given shift
    offset. Lower case letters should remain lower case, upper case
    letters should remain upper case, and all other punctuation should
    stay as it is.

    text: string to apply the shift to
    shift: amount to shift the text (0 <= int < 26)
    returns: text after being shifted by specified amount.
    """
    return applyCoder(text, buildCoder(shift))


def findBestShift(wordList, text):
    """
    Finds a shift key that can decrypt the encoded text.

    text: string
    returns: 0 <= int < 26
    """
    real_words = 0
    best_shift = 0
    shift = 0
    for shift in range(0, 26):
        result_list = []
        counter = 0
        new_text = applyShift(text, shift)
        for word in new_text.split(" "):
            result_list.append(word)

        for word in result_list:
            if word in wordList:
                counter += 1
            if counter > real_words:
                real_words = counter
                best_shift = shift
    return best_shift
