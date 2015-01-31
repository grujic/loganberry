# Basic imports
import sys
import argparse
from time import sleep

# Our imports
from lib.defs import ExchangeConnection
from strategies.bank_class import Bank
from strategies.quotes_class import Quotes
from strategies.algorithms import buy_everything_at_best_ask
from strategies.algorithms import sell_everything_at_best_bid
from strategies.logic import refresh_quotes

from lib.book import Book

PUBLIC_EXCHANGE_PUBLIC_IP = "54.154.191.94"
PUBLIC_EXCHANGE_PUBLIC_IP = "10.0.129.254"

parser = argparse.ArgumentParser(description='Main script for the loganberry team.')
parser.add_argument('exchange_host',
                    metavar='host',
                    type=str,
                    default='10.0.129.254',
                    help='Host IP, default is 10.0.129.254')
parser.add_argument('port_index',
                    metavar='port',
                    type=int,
                    default=25000,
                    help='Port, default is 25000')

args = parser.parse_args()


### Read in command line arguments ###
print("\n\n")
print("exchange host address = " + args.exchange_host + "\n\n")
print("port index = " + str(args.port_index) + "\n\n")

### Instantiate connection to the exchange ###

market_has_opened = False

conn = ExchangeConnection(args.exchange_host, 25000 + int(args.port_index))
conn.sayHello()
print 'Entering loop'

x = 0
while True:
    conn.update()
    
    if conn.market_open is False and market_has_opened is False:
        print "Market isn't open... looping..."
        sleep(0.2)
        continue
    elif conn.market_open is False and market_has_opened is True:
        print "Market has now closed."
        sys.exit(0)    
    
    market_has_opened = True
    
    
    x += 1
    #for x in xrange(10):
    print 'Iteration {}'.format(x)
    conn.update()
    # refresh_quotes(conn)

    if x == 1:
        conn.bank.print_portfolio()
        #conn.addOrder('QUUX', 'BUY', 1, 50)
        #conn.addOrder('QUUX', 'BUY', 10000, 50)
        buy_everything_at_best_ask(conn)
        sell_everything_at_best_bid(conn)

    print "Current quotes are: "
    print conn.quotes.printQuotes()
            
conn.bank.print_portfolio()
# conn.book.update_ticker_data("FOO", {'buy': [[3367,100],[3359,100],[3355,300],[3349,300],[3348,100],[3347,100],[3344,300],[3343,100],[3338,200],[3335,100],[3318,200],[3313,200]], 'sell': [[3367,100],[3359,100],[3355,300],[3349,300],[3348,100],[3347,100],[3344,300],[3343,100],[3338,200],[3335,100],[3318,200],[3313,200]]})
# conn.book.update_ticker_data("BAR", {'buy': [[1,100],[1,100],[1,300],[1,300],[321,100],[432,100],[432,300],[654,100],[156,200],[654,100],[23,200],[423,200]], 'sell': [[65,100],[34,100],[134,300],[65,300],[6547,100],[134,100],[234,300],[56,100],[54,200],[45,100],[13,200],[76,200]]})

# buy_everything_at_best_ask(conn)
# sell_everything_at_best_bid(conn)
