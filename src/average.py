class Average():
	def get_average(self, value_list):
		return sum(value_list) / (len(value_list) - 1)

value = 1
value_list = []
while value != 0:
	value = float(input("Enter a value and press Enter. Enter '0' if there are no more values. > "))
	value_list.append(value)
	if value == 0:
		if value_list[0] != "0":
			GivenValues = Average()
			print GivenValues.get_average(value_list)
		else:
			print "'0' is not a valid first entry."