def are_anagrams(str1, str2):
    return sorted(str1) == sorted(str2)

print are_anagrams("god", "dog")
