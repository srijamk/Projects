class VowelOrConsonant():
    def get_letter(self, letter):
        return str(letter) in ['a', 'e', 'i', 'o', 'u']

letter = str(input("Enter a letter: "))
Letter = VowelOrConsonant()
if Letter.get_letter(letter) == True:
    print "Vowel"
elif letter == "y":
    print "Y is sometimes a vowel and sometimes a consonant."
else:
    print "Consonant"
