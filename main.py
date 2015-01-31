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

book = Book()

conn.sayHello()

quotes = Quotes()
bank = Bank()
book = Book()

book.update_ticker_data("FOO", {'buy': [[3367,100],[3359,100],[3355,300],[3349,300],[3348,100],[3347,100],[3344,300],[3343,100],[3338,200],[3335,100],[3318,200],[3313,200]], 'sell': [[3367,100],[3359,100],[3355,300],[3349,300],[3348,100],[3347,100],[3344,300],[3343,100],[3338,200],[3335,100],[3318,200],[3313,200]]})

buy_algo(conn, bank, book, quotes)
