class Quote:
	# Class to keep track of current outstanding quotes

	def __init__(self, ticker, direction, quote_type, price, size, quote_id):
		self.ticker = ticker
		self.direction = direction
		self.quote_type = quote_type
		self.size = size
		self.price = price
		self.quote_id = quote_id

	def printQuote(self):
		print self.ticker + " | " + self.direction + " | " + self.quote_type + " | " + self.size + " | " + self.price + " | " + self.quote_id


class Quotes:
	def __init__(self):
		self.quotes = [ ]

	def addQuote(self, quote):
		self.quotes.append(quote)

	def removeQuote(self, quote_id):
		self.quotes = [ q for q in self.quotes if q.id != quote_id ]

	def getID(self, ticker, direction, quote_type):
		pass

	def acknowledgeQuote(self, quote_id):
		pass

	def printQuotes(self):
		print " Ticker | Direction | Quote Type | Size | Price | Quote ID "

		for quote in self.quotes:
			quote.printQuote()


