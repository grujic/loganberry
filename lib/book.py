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
        buy_data = self.get_ticker_buy_data(ticker)
        if len(buy_data) ==0 :
            return -1
        else:
            return sorted(buy_data, key = lambda x: x[0])[0]

    def get_best_sell_quote(self, ticker):
        sell_data = self.get_ticker_sell_data(ticker)
        if len(sell_data) ==0 :
            return -1
        else:
            return sorted(sell_data, key = lambda x: x[0])[0]

    def nth_buy_price(self, ticker, n):
        return sorted(self.get_ticker_buy_data(ticker), key = lambda x: x[0])[-n][0]

    def nth_sell_price(self, ticker, n):
        return sorted(self.get_ticker_sell_data(ticker), key = lambda x: x[0])[n][0]

    def mean_buy_volume(self, ticker):
        sizes = self.get_ticker_buy_volumes(ticker)
        if len(sizes) > 0:
            return 1.0*sum(sizes)/len(sizes)
        else:
            return 0

    def mean_sell_volume(self, ticker):
        sizes = self.get_ticker_sell_volumes(ticker)
        if len(sizes) > 0:
            return 1.0*sum(sizes)/len(sizes)
        else:
            return 0

    def get_vwap_sell_price(self, ticker, shares):
        vwap = 0
        need_to_buy = shares

        sell_data = self.get_ticker_sell_data(ticker)
        
        print sell_data

        sorted(self.get_ticker_sell_data(ticker), key = lambda x: x[0])[0]

        print sell_data

        i = 0

        for quote in sell_data:
            price = quote[0]
            size = quote[1]

            if(size >= need_to_buy):
                vwap += need_to_buy * price
                need_to_buy = 0
            else:
                vwap += size * price / shares
                need_to_buy -= size

            i++