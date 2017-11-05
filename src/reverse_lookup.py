class ReverseLookup():
    def get_key(self, dictionary, value):
        key_list = []
        for key in dictionary:
            if dictionary[key] == value:
                # If the key matches the parameter value, append key to the list
                key_list.append(key)
        return key_list

    def main(self):
        dictionary = {
        "apples": "disgusting",
        "bananas": "disgusting",
        "cherries": "yummy",
        "mangoes": "very yummy",
        "pineapples": "very yummy",
        "oranges": "yummy",
        "tangerines": "very yummy",
        "pomegranates": "very disgusting",
        "pears": "extremely disgusting"
        }
        # Will return mangoes, pineapples, and tangerines
        print self.get_key(dictionary, "very yummy")
if __name__ == '__main__':
    print ReverseLookup().main()
