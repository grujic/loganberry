from strategies.bank_class import Bank
from lib.defs import ExchangeConnection




def buy_algo(conn, bank, book, quotes):
	print "buy algo function ran"
	
	book_data = book.get_ticker_data("FOO")

	buy_orders = sorted(book_data["buy"], key=lambda x: x[1], reverse=True)

	print "Foo is available at " + str(buy_orders[0][0]) + ". " + str(buy_orders[0][1]) + " shares."

	
	# if(false):
	# 	test_direction = "BUY"
	# 	test_quote_type = "Beta"
	# 	test_price = 15
	# 	test_num_shares = 100

	# 	order_id = conn.addOrder(test_ticker, test_direction, test_price, test_num_shares)

	# 	test_quote = Quote(test_ticker, test_direction, test_quote_type, test_num_shares, test_price, order_id)

	# 	quotes.addQuote(test_quote)