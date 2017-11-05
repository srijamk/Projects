class PigLatin():
    vowels = ["a", "e", "i", "o", "u", "y", "A", "E", "I", "O", "U", "Y"]
    invalid_character_list = [":", ".", "?", "-", "'", "!", ":", ";"]
    def convert_to_pig_latin(self, sentence):
        has_upper = False
        return_sentence = ""
        for character in sentence:
            if character in self.invalid_character_list:
                sentence = sentence.replace(character, "")
        if sentence != sentence.lower():
            has_upper = True
            sentence = sentence.lower()

        for word in sentence.split(" "):
            if word[0] in self.vowels:
                word = word + "way"
                return_sentence += word
            if word[0] not in self.vowels:
                word = self.convert_from_consonants(word)

                return_sentence += word
        if has_upper:
            return_sentence = return_sentence[0].upper() + return_sentence[1:len(return_sentence)]
        return return_sentence + character

    def convert_from_consonants(self, word):
        index = 0
        while index < len(word):
            if word[index] in self.vowels:
                return word[index:len(word)] + word[0:index] + "ay"
            index += 1

sentence = raw_input("Enter a sentence: ")
print PigLatin().convert_to_pig_latin(sentence)
