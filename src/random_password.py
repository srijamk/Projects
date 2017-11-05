import random
class RandomPassword():
    SHORTEST_LENGTH = 7
    LONGEST_LENGTH = 10
    MIN_ASCII = 33
    MAX_ASCII = 127
    def get_random_password(self):
        password = ""
        # Length of password must be between 7 and 10, inclusive
        length = random.randint(self.SHORTEST_LENGTH, self.LONGEST_LENGTH)
        for x in range(length):
            # Generates random character given min and max of ascii nums
            character = random.randint(self.MIN_ASCII, self.MAX_ASCII)
            password += str(chr(character))
        return password

    def main(self):
        print self.get_random_password()

if __name__ == '__main__':
    Password().main()
