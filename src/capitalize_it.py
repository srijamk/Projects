class Capitalize():
    def get_capitalized_string(self, string):
        to_capitalize = [" i ", string[0]]
        result = ""
        cap = True
        for char in string:
            if cap:
                result += char.upper()
                if char == " ":
                    cap = True
                else:
                    cap = False
                continue

            if char == '.' or char == '?' or char == "!":
                cap = True
            else:
                cap = False

            if char == "i":
                cap = False

            result += char

            #if char not in to_capitalize and not((". " + char) in string or ("? " + char) in string or ("! " + char) in string):
            #    result += char
            #else:
            #    result += char.upper()
        return result

string = raw_input("Enter a string: ")
GivenString = Capitalize()
print GivenString.get_capitalized_string(string)
