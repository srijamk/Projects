class HeatCapacity():
    WATER_HEAT_CAPACITY = 4.186
    COST_PER_KILOWATT_HOUR = 8.9
    JOULES_TO_KILOWATT_HOURS = 2.777e-7
    def get_amount_of_energy(self, mass, temperature_change):
        return mass * temperature_change * self.WATER_HEAT_CAPACITY

    def get_cost_of_boiling_water(self):
        energy_in_joules = self.get_amount_of_energy(150, 100)
        return "Energy costs $%.2f." \
        % (self.COST_PER_KILOWATT_HOUR * (energy_in_joules * self.JOULES_TO_KILOWATT_HOURS))

mass = float(input("Enter your mass: "))
temperature_change = float(input("Enter the desired temperature change: "))
energy_calc = HeatCapacity()
print energy_calc.get_amount_of_energy(mass, temperature_change)
print energy_calc.get_cost_of_boiling_water()
