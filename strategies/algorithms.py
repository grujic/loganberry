from strategies.bank_class import Bank
from lib.defs import ExchangeConnection
from strategies.quotes_class import Quote


def buy_everything_at_best_ask(conn):
	print "Running buy_everything_at_best_ask() function"

	tickers = [ "FOO", "BAR", "BAZ", "QUUX", "CORGE" ]
	size = 100

	for ticker in tickers:
		best_sell_quote = conn.book.get_best_sell_quote(ticker)

		print "Best sell quote for " + ticker + " is " + str(best_sell_quote)
		print conn.book.get_ticker_sell_data(ticker)

		order_id = conn.addOrder(ticker, "BUY", 0.9 * best_sell_quote[0], size)

		quote_record = Quote(ticker, "BUY", "Alpha", 0.9 * best_sell_quote[0], size, order_id)
		conn.quotes.addQuote(quote_record)


def sell_everything_at_best_bid(conn):
	print "Running sell_everything_at_best_bid() function"

	tickers = [ "FOO", "BAR", "BAZ", "QUUX", "CORGE" ]
	size = 100

	for ticker in tickers:
		best_buy_quote = conn.book.get_best_buy_quote(ticker)

		print "Best sell quote for " + ticker + " is " + str(best_buy_quote)
		print conn.book.get_ticker_buy_data(ticker)

		order_id = conn.addOrder(ticker, "SELL", 1.1 * best_buy_quote[0], size)

		quote_record = Quote(ticker, "SELL", "Alpha", 1.1 * best_buy_quote[0], size, order_id)
		conn.quotes.addQuote(quote_record)