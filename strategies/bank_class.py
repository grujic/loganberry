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

