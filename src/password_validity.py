import string
class PasswordValidity():
    def get_validity(self, password):
        upper_counter = 0
        lower_counter = 0
        number_counter = 0
        for character in password:
            if character in string.ascii_uppercase:
                upper_counter += 1
            elif character in string.ascii_lowercase:
                lower_counter += 1
            elif character in str(range(1, 10)):
                number_counter += 1

        return (upper_counter > 0 and lower_counter > 0 and number_counter > 0 and len(password) >= 8)


    def main(self):
        password = raw_input("Enter a password: ")
        if self.get_validity(password):
            print "%s is a valid password. " % password
        else:
            print "%s is not a valid password. " % password

if __name__ == '__main__':
    Password().main()
