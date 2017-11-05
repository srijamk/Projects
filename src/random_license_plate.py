import random
class LicensePlate():
    MIN_ASCII = 65
    MAX_ASCII = 90
    # 4 numbers followed by 3 numbers ex: 1234ABC
    def get_new_license_plate(self):
        license_plate_number = ""
        for x in range(4):
            license_plate_number += str(random.randint(1, 9))
        for x in range(3):
            license_plate_number += chr(random.randint(self.MIN_ASCII, self.MAX_ASCII))
        return license_plate_number

    # 3 letters followed by 3 numbers ex: ABC123
    def get_old_license_plate(self):
        license_plate_number = ""
        for x in range(3):
            license_plate_number += chr(random.randint(self.MIN_ASCII, self.MAX_ASCII))

        for x in range(3):
            license_plate_number += str(random.randint(1, 9))

        return license_plate_number

    def main(self):
        if random.randint(1, 2) == 1:
            print "Your new license plate is %s." % self.get_new_license_plate()
        else:
            print "Your old license plate number is %s." % self.get_old_license_plate()

if __name__ == '__main__':
    LicensePlate().main()
