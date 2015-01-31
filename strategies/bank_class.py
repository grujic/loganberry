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

		def update(self, ticker, price, size):
			vwap = ( self.prices[ticker] * self.positions[ticker] + size * price ) / (self.positions[ticker] + size)

			self.prices[ticker] = vwap
			self.positions[ticker] += size