import math

class FreeFall():
    ACCELERATION = 9.8
    def get_final_velocity(self, init_speed, distance):
        return "Object will be traveling %.2f m/s when it hits the ground." %\
        math.sqrt(init_speed ** 2 + 2 * self.ACCELERATION * distance)

init_speed = int(input("Enter the initial speed of the object: "))
distance = int(input("Enter the distance travelled by the object: "))
measurements = FreeFall()
print measurements.get_final_velocity(init_speed, distance)
