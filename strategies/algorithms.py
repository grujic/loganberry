from strategies.bank_class import Bank
from lib.defs import ExchangeConnection
from strategies.quotes_class import Quote


def buy_everything_at_best_ask(conn):
	print "Running buy_everything_at_best_ask() function"

	tickers = [ "FOO", "BAR", "BAZ", "QUUX", "CORGE" ]
	size = 100

	for ticker in tickers:
		best_sell_quote = conn.book.get_best_sell_quote(ticker)

        if best_sell_quote == -1:
            return

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

    	if best_buy_quote == -1:
            return

        print "Best sell quote for " + ticker + " is " + str(best_buy_quote)
        print conn.book.get_ticker_buy_data(ticker)

        order_id = conn.addOrder(ticker, "SELL", 1.1 * best_buy_quote[0], size)

        quote_record = Quote(ticker, "SELL", "Alpha", 1.1 * best_buy_quote[0], size, order_id)
        conn.quotes.addQuote(quote_record)

def arbitrage_CORGE(conn):
	print "Running arbitrage_CORGE() function"

	multiplier = 1000

	for num_shares in xrange (multiplier, 100, -100):

		corge_avg_price = conn.book.get_vwap_buy_price("CORGE", multiplier)
		foo_avg_price = conn.book.get_vwap_sell_price("FOO", multiplier)
		bar_avg_price = conn.book.get_vwap_sell_price("BAR", multiplier)

		print "corge_sell_price: " + str(corge_avg_price)
		print "foo_buy_price: " + str(foo_avg_price)
		print "bar_buy_price: " + str(bar_avg_price)

		corge_sell_price = multiplier * corge_avg_price
		foo_buy_price = multiplier * 0.3 * foo_avg_price
		bar_buy_price = multiplier * 0.8 * bar_avg_price

		if(corge_sell_price > foo_buy_price + bar_buy_price + 100):
			#Buy Foo:
			order_id = conn.addOrder("FOO", "BUY", 9999999, multiplier)
			quote_record = Quote("FOO", "BUY", "Arb", 9999999, multiplier, order_id)
			conn.quotes.addQuote(quote_record)

			#Buy Bar:
			order_id = conn.addOrder("BAR", "BUY", 9999999, multiplier)
			quote_record = Quote("BAR", "BUY", "Arb", 9999999, multiplier, order_id)
			conn.quotes.addQuote(quote_record)

			#Sell Corge:
			order_id = conn.addOrder("CORGE", "SELL", 0, multiplier)
			quote_record = Quote("CORGE", "SELL", "Arb", 0, multiplier, order_id)
			conn.quotes.addQuote(quote_record)

			#Convert Corge:
			conn.convertOrder("CORGE", "BUY", multiplier)


		corge_avg_price = conn.book.get_vwap_sell_price("CORGE", multiplier)
		foo_avg_price = conn.book.get_vwap_buy_price("FOO", multiplier)
		bar_avg_price = conn.book.get_vwap_buy_price("BAR", multiplier)

		print "corge_buy_price: " + str(corge_avg_price)
		print "foo_sell_price: " + str(foo_avg_price)
		print "bar_sell_price: " + str(bar_avg_price)

		corge_buy_price = multiplier * corge_avg_price
		foo_sell_price = multiplier * 0.3 * foo_avg_price
		bar_sell_price = multiplier * 0.8 * bar_avg_price

		if(corge_buy_price < foo_sell_price + bar_sell_price - 100):
			#Sell Foo:
			order_id = conn.addOrder("FOO", "SELL", 0, multiplier)
			quote_record = Quote("FOO", "SELL", "Arb", 0, multiplier, order_id)
			conn.quotes.addQuote(quote_record)

			#Sell Bar:
			order_id = conn.addOrder("BAR", "SELL", 0, multiplier)
			quote_record = Quote("BAR", "SELL", "Arb", 0, multiplier, order_id)
			conn.quotes.addQuote(quote_record)

			#Buy Corge:
			order_id = conn.addOrder("CORGE", "BUY", 9999999, multiplier)
			quote_record = Quote("CORGE", "BUY", "Arb", 9999999, multiplier, order_id)
			conn.quotes.addQuote(quote_record)

			#Convert Corge:
			conn.convertOrder("CORGE", "SELL", multiplier)
