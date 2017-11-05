import sys

class DogYears():
    DOG_CHILDHOOD_YEARS = 5.25
    def get_dog_years(self, human_years):
        if human_years < 0:
            raise Exception("Negative ages are invalid. Please enter a positive age.")
        elif 0 <= human_years <= 2:
            return self.DOG_CHILDHOOD_YEARS * human_years
        else:
            return self.DOG_CHILDHOOD_YEARS * human_years + 4 * (human_years - 2)


human_years = int(input("Enter age in human years: "))
age = DogYears()
try:
    print age.get_dog_years(human_years)
except:
    e = sys.exc_info()[0]
    print e
