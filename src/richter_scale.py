class RichterScale():
    def get_descriptor(self, magnitude):
        magnitudes = {
        (0, 1.9):"Micro",
        (2.0, 2.9):"Very Minor",
        (3.0, 3.9):"Minor",
        (4.0, 4.9):"Light",
        (5.0, 5.9):"Moderate",
        (6.0, 6.9):"Strong",
        (7.0, 7.9):"Major",
        (8.0, 9.9):"Great"
        }
        if magnitude >= 10.0:
            return "Meteoric"
        for key in magnitudes.keys():
            if key[0] <= magnitude <= key[1]:
                return magnitudes[key]

magnitude = float(input("Enter a earthquake magnitude: "))
givenMagnitude = RichterScale()
print givenMagnitude.get_descriptor(magnitude)
