class Bank:
	# Class to keep track of cash and portfolio positions

	def __init__(self):
		self.cash = 0;
		
		self.positions = {
			"FOO" : 0, "BAR" : 0, "BAZ" : 0, "QUUX" : 0, "CORGE" : 0
		}
		
		self.prices = {
			"FOO" : 0, "BAR" : 0, "BAZ" : 0, "QUUX" : 0, "CORGE" : 0
		}

	def update(self, ticker, price, size, direction):
		if (direction == "BUY"):
			dir_integer = 1
		else:
			dir_integer = -1
		
		self.cash += -1 * dir_integer * size * price

		if (self.positions[ticker] + dir_integer * size == 0):
			vwap = 0
		else:
			vwap = ( self.prices[ticker] * self.positions[ticker] + dir_integer * size * price ) / (self.positions[ticker] + dir_integer * size)

		self.prices[ticker] = vwap
		self.positions[ticker] += dir_integer * size

	def print_portfolio(self):
		print "Portfolio value: " + str(self.cash)
		print self.positions
		print self.prices