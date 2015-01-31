class Book:
	# Representation of the book
	def __init__(self):
		self.tickers = ["FOO", "BAR", "BAZ", "QUUX", "CORGE"]
		self.data = {ticker: {'buy': [], 'sell': []} for ticker in self.tickers}

	def update_ticker_data(self, ticker, new_data):
		self.data[ticker] = new_data

	def get_ticker_data(self, ticker):
		return self.data[ticker]

	def get_ticker_buy_data(self, ticker):
		return self.data[ticker].get('buy', [])

	def get_ticker_sell_data(self, ticker):
		return self.data[ticker].get('sell', [])