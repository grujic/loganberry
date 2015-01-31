from strategies.bank_class import Bank
from lib.defs import ExchangeConnection
from strategies.quotes_class import Quote



def buy_algo(conn, bank, quotes):
	print "Running buy algo function"

	best_buy_quote = conn.book.get_best_buy_quote("FOO")
	
	print best_buy_quote
	
	if(True):
		order_id = conn.addOrder("FOO", "BUY", best_buy_quote[0], best_buy_quote[1])

		quote_record = Quote("FOO", "BUY", "Beta", best_buy_quote[0], best_buy_quote[1], order_id)

		quotes.addQuote(quote_record)