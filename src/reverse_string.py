def reverse_string(word):
    result = ""
    for index in range(0, len(word)):
        result += word[(len(word) - 1) -index]
    return result

print reverse_string("hello")
