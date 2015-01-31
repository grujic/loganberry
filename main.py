# Basic imports
import sys

# Our imports
from lib.defs import ExchangeConnection
from strategies.bank_class import Bank
from strategies.quotes_class import Quotes
from strategies.algorithms import buy_algo
from lib.book import Book

PUBLIC_EXCHANGE_PUBLIC_IP = "54.154.191.94"
PUBLIC_EXCHANGE_PUBLIC_IP = "10.0.129.254"

exchange_host = sys.argv[1]
port_index = sys.argv[2]

### Read in command line arguments ###
print("\n\n")
print("exchange host address = " + exchange_host + "\n\n")
print("port index = " + port_index + "\n\n")

### Instantiate connection to the exchange ###
conn = ExchangeConnection(exchange_host, 25000 + int(port_index))

conn.sayHello()

conn.book.update_ticker_data("FOO", {'buy': [[3367,100],[3359,100],[3355,300],[3349,300],[3348,100],[3347,100],[3344,300],[3343,100],[3338,200],[3335,100],[3318,200],[3313,200]], 'sell': [[3367,100],[3359,100],[3355,300],[3349,300],[3348,100],[3347,100],[3344,300],[3343,100],[3338,200],[3335,100],[3318,200],[3313,200]]})
conn.book.update_ticker_data("BAR", {'buy': [[1,100],[1,100],[1,300],[1,300],[321,100],[432,100],[432,300],[654,100],[156,200],[654,100],[23,200],[423,200]], 'sell': [[65,100],[34,100],[134,300],[65,300],[6547,100],[134,100],[234,300],[56,100],[54,200],[45,100],[13,200],[76,200]]})

buy_everything_at_best_ask(conn)
sell_everything_at_best_bid(conn)