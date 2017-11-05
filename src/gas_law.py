class GasLaw():
    R = 8.314
    def get_gas_in_moles(self, pressure, volume, temperature):
        return "The amount of gas is %.2f moles." % ((pressure * volume) \
        / (self.R * temperature))

pressure = int(input("Enter the amount of pressure in Pascals: "))
volume = int(input("Enter the volume: "))
temperature = int(input("Enter the temperature in Kelvin: "))
measurements = GasLaw()
print measurements.get_gas_in_moles(pressure, volume, temperature)
