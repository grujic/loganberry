class Book:
    # Representation of the book
    def __init__(self):
        self.tickers = ["FOO", "BAR", "BAZ", "QUUX", "CORGE"]
        self.data = {ticker: {'buy': [], 'sell': []} for ticker in self.tickers}

    def update_ticker_data(self, ticker, new_data):
        self.data[ticker] = new_data

    def update_ticker_buy_data(self, ticker, new_data):
        self.data[ticker]['buy'] = new_data

    def update_ticker_sell_data(self, ticker, new_data):
        self.data[ticker]['sell'] = new_data

    def get_ticker_data(self, ticker):
        return self.data[ticker]

    def get_ticker_buy_data(self, ticker):
        return self.data[ticker].get('buy', [])

    def get_ticker_sell_data(self, ticker):
        return self.data[ticker].get('sell', [])

    def get_ticker_buy_prices(self, ticker):
        return [el[0] for el in self.data[ticker]['buy']]

    def get_ticker_buy_volumes(self, ticker):
        return [el[1] for el in self.data[ticker]['buy']]

    def get_ticker_sell_prices(self, ticker):
        return [el[0] for el in self.data[ticker]['sell']]

    def get_ticker_sell_volumes(self, ticker):
        return [el[1] for el in self.data[ticker]['sell']]

    def get_best_buy_quote(self, ticker):
        return sorted(self.get_ticker_buy_data(ticker), key = lambda x: x[0])[-1]

    def get_best_sell_quote(self, ticker):
        return sorted(self.get_ticker_sell_data(ticker), key = lambda x: x[0])[0]

    def nth_buy_price(self, ticker, n):
        pass

    def nth_sell_price(self, ticker, n):
        pass

    def mean_buy_volume(self, ticker):
        pass

    def mean_sell_volume(self, ticker):
        pass