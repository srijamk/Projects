class DistanceUnits():
    INCHES = 12.0
    YARDS = 3.0
    MILES = 5820.0
    def get_distance_in_inches_yards_and_miles(self, feet):
        return "%d inches, %.5f yards, and %.5f miles. " % (feet * self.INCHES, feet / \
        self.YARDS, feet / self.MILES)

height_in_feet = float(input("Enter height in feet: "))
height = DistanceUnits()
print height.get_distance_in_inches_yards_and_miles(height_in_feet)
