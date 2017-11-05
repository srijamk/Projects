import random
class Roulette():
	color_to_number = {
	"Red": (1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36),
	"Black": (2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35),
	"Green": (0, "00")
	}
	def get_payout(self):
		possible_numbers = ["00"]
		for x in range(0, 37):
			possible_numbers.append(x)
		number = random.choice(possible_numbers)
		print "The spin resulted in %s" % number
		print 
		
	def red_vs_black(self, number):
		for key in self.color_to_number.keys():
			if number in self.color_to_number[key]:
				print key
				
	def odd_or_even(self, number):
		message = "Pay Odd"
		if number % 2 == 0:
			message = "Pay Even"
		elif number == 0 or number == "00":
			message = ""
		print message
		
	def get_range(self, number):
		range = "Pay 1 to 18"
		if 19 <= number <= 36:
			range = "Pay 19 to 36"
		elif number == 0 or number == "00":
			range = ""
		print range
		
GivenWheel = Roulette()
print GivenWheel.get_payout()