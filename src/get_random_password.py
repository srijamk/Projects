from random_password import RandomPassword
from password_validity import PasswordValidity
class GoodPassword():
    def get_random_password(self):
        number_of_attempts = 1
        password = RandomPassword().get_random_password()
        while PasswordValidity().get_validity(password) == False:
            password = RandomPassword().get_random_password()
            number_of_attempts += 1
        return "%s was generated after %i attempts. " % (password, number_of_attempts)

print GoodPassword().get_random_password()
