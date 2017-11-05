class Taxi():
    BASE_FARE = 4.0
    RATE = 0.25
    def get_fare(self, kilometers):
        return "Fare is $%.2f." % float(self.BASE_FARE + self.RATE * (1000 * kilometers / 140))

kilometers = float(raw_input("Enter a distance in kilometers: "))
GivenDistance = Taxi()
print GivenDistance.get_fare(kilometers)
