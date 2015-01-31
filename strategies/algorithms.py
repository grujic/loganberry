from strategies.bank_class import Bank
from lib.defs import ExchangeConnection




def buy_algo(conn, bank, book, quotes):
	print "Running buy algo function"

	best_buy_quote = book.get_best_buy_quote("FOO")
	
	print best_price
	
	if(true):
		order_id = conn.addOrder("FOO", "BUY", best_buy_quote[0], best_buy_quote[1])

		quote_record = Quote("FOO", "BUY", "Beta", best_buy_quote[1], best_buy_quote[0], order_id)

		quotes.addQuote(quote_record)