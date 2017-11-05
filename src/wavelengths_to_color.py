class WaveLengths():
	wavelengths = {
	(380, 449): "Violet",
	(450, 494): "Blue",
	(495, 569): "Green",
	(570, 589): "Yellow",
	(590, 619): "Orange",
	(620, 750): "Red"
	}
	def get_color(self, wavelength):
		for key in self.wavelengths.keys():
			if key[0] <= wavelength <= key[1]:
				return self.wavelengths[key]
		if wavelength < 380 or wavelength > 750:
			return "Invalid wavelength"
			
wavelength = int(raw_input("Enter a wave length: "))
GivenWavelength = WaveLengths()
print GivenWavelength.get_color(wavelength)