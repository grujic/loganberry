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
        print self.ticker + " | " + self.direction + " | " + self.quote_type + " | " + str(self.size) + " | " + str(self.price) + " | " + str(self.quote_id)


class Quotes:
    def __init__(self):
        self.quotes = [ ]

    def addQuote(self, quote):
        self.quotes.append(quote)

    def removeQuote(self, quote_id):
        self.quotes = [ q for q in self.quotes if q.id != quote_id ]

    def getID(self, ticker, direction, quote_type):
        matches = [ q for q in self.quotes if q.ticker == ticker and q.direction == direction and q.quote_type == quote_type ]
        if (len(matches) == 0):
            return -1
        else:
            return matches[0].quote_id

    def getPrice(self, quote_id):
        matches = [ q for q in self.quotes if
                         q.quote_id == quote_id ]
        if (len(matches) == 0):
            return -1
        else: 
            return matches[0].price

    def acknowledgeQuote(self, quote_id):
        pass

    def printQuotes(self):
        print " Ticker | Direction | Quote Type | Size | Price | Quote ID "

        for quote in self.quotes:
            quote.printQuote()


