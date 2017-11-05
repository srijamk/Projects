class HeightUnits():
    def get_height_in_centimeters(self, height):
        return str(height[0] * 30.48 + height[1] * 2.54) + " cm"

heights = list(input("Enter your height with feet and inches separated by a comma: "))
height_in_feet = HeightUnits()
print height_in_feet.get_height_in_centimeters(heights)
