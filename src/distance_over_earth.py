import math

class Distance():
    def get_distance(self, t1, g1, t2, g2):
        return 6371.01 * math.acos(math.sin(t1) * math.sin(t2) + math.cos(t1) * math.cos(t2) * math.cos(g1 - g2))

t1 = math.radians(int(input("Enter the x-value of the first coordinate: ")))
g1 = math.radians(int(input("Enter the y-value of the first coordinate: ")))
t2 = math.radians(int(input("Enter the x-value of the second coordinate: ")))
g2 = math.radians(int(input("Enter the y-value of the second coordinate: ")))

coordinates = Distance()
print coordinates.get_distance(t1, g1, t2, g2)
