class Cylinder():
    PI = 3.14
    def get_cylinder_volume(self, radius, height):
        return "Volume is %.1f." % self.PI * radius ** 2 * height

radius = int(input("Enter your radius: "))
height = int(input("Enter your height: "))
measurements = Cylinder()
print measurements.get_cylinder_volume(radius, height)
