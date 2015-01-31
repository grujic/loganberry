from strategies.bank_class import Bank
from lib.defs import ExchangeConnection




def buy_algo(conn, bank, book, quotes):
	print "Running buy algo function"

	best_price = book_data.get_best_buy_price("FOO")
	print best_price
	
	# if(false):
	# 	test_direction = "BUY"
	# 	test_quote_type = "Beta"
	# 	test_price = 15
	# 	test_num_shares = 100

	# 	order_id = conn.addOrder(test_ticker, test_direction, test_price, test_num_shares)

	# 	test_quote = Quote(test_ticker, test_direction, test_quote_type, test_num_shares, test_price, order_id)

	# 	quotes.addQuote(test_quote)