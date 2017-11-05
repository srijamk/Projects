class Anagram():
    def are_anagrams(self, word1, word2):
        sorted_word1 = []
        sorted_word2 = []
        for char in word1:
            if char != " ":
                sorted_word1.append(char.lower())
        for char in word2:
            if char != " ":
                sorted_word2.append(char.lower())
        sorted_word1 = sorted(sorted_word1)
        sorted_word2 = sorted(sorted_word2)
        return str(sorted_word1 == sorted_word2)

    def main(self):
        # Should return False, True, True
        return self.are_anagrams("eviler", "live") + "\n" + self.are_anagrams("anagram", "nag a ram") + "\n" + self.are_anagrams("William Shakespeare", "I am a weakish speller")

print Anagram().main()
