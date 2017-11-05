class Discount():
	DISCOUNT_AMOUNT = 0.6
	PERCENT_AFTER_MARKDOWN = 0.4
	def get_discount_table(self):
		price_list = [4.95, 9.95, 14.95, 19.95, 24.95]
		for price in price_list:
			print "%.2f | %.2f | %.2f" % (price, price * self.DISCOUNT_AMOUNT, price * self.PERCENT_AFTER_MARKDOWN)
			
GivenPrices = Discount()
print GivenPrices.get_discount_table()
		