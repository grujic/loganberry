import socket
import json
import logging
from logging import handlers

from lib.book import Book

# Set up logging: (this uses old-style formatting)
formatStr = '[%(asctime)s]  %(levelname)-7s (%(filename)s:%(lineno)d) %(funcName)s - %(message)s'
dateFmtStr = '%d %b %H:%M:%S'
#logging.basicConfig(format=formatStr, 
                    #datefmt='%d %b %H:%M:%S', 
                    #level=logging.INFO)
# create logger
logger = logging.getLogger('loganberry')
logger.setLevel(logging.DEBUG)

# create console handler and set level to debug
#ch = logging.FileHandler('test.log')
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
formatter = logging.Formatter(formatStr,
                              dateFmtStr)  # create formatter
ch.setFormatter(formatter)                # add formatter to ch
#logger.addHandler(ch)                     # add ch to logger

# Add a file logger:
fh = logging.handlers.TimedRotatingFileHandler('main.log',
                                                when='midnight',
                                                backupCount=7)
fh.setLevel(logging.DEBUG)
fh.setFormatter(formatter)                # add formatter to ch
#logger.addHandler(fh)                     # add ch to logger

# Add root logger to both handlers: get all messages to console AND file.
rootlogger = logging.getLogger()
rootlogger.addHandler(ch)
rootlogger.addHandler(fh)


class ExchangeConnection:
    # Main class for interacting with the exchange

    def __init__(self, host='10.0.129.254', port=25000, start_immediately=True):
        self.host = host
        self.port = port
        if start_immediately:
            self.s = self._startConnection()
        self.book = Book()
        self.next_order_id = 0
        
        logger.debug('Starting up.')

    def addOrder(self, stock_ticker, dir, price, size):
        self.next_order_id += 1

        # Add an order
        json_struct = { \
            "type": "add", \
            "order_id": self.next_order_id, \
            "symbol": stock_ticker, \
            "dir": dir, \
            "price": price, \
            "size": size \
        }

        #resp = self._send_and_receive(json_struct)

        return self.next_order_id

    def convertOrder(self):
        # Convert an ETH to its components
        pass

    def cancelOrder(self):
        # Cancel an order
        pass

    def sayHello(self):
        # Check connection
        ### TEMP ###
        ehlo = {"type": "hello", "team": "LOGANBERRY"}
        # resp = self._send_and_receive(ehlo)
        self._send(ehlo)
        
    def update(self):
        # Receives data from network stream, updates
        # linked Book class instance.
        logger.debug('Enter.')
        lines = self._readlines(lines_to_read=10)
        
        for line in lines:
            self.parse(line)
            
    def parse(self, line):
        # Workhorse function to parse lines returned
        # from server.
        print 'Parsing line: '
        print line
        try:
            parsed_json = json.loads(line)
        except:
            logger.error('Incomplete line!')
            return

        if parsed_json['type'] == "book":

            ticker = parsed_json['symbol']
            buy_sell_data = {'sell': parsed_json['sell'], 'buy': parsed_json['buy']}

            logger.info("buy_sell_data for ticker " + ticker + " = ")
            logger.info(str(buy_sell_data))

            self.book.update_ticker_data(ticker, buy_sell_data)

        else:
            logger.error("Don't know how to process type = " + parsed_json['type'])

    ### Lower level communications ###
    def _fromJSON(self, json_struct):
        return json.dumps(json_struct) + '\n'

    def _startConnection(self):
        # Open a socket connection
        s = socket.socket()
        s.connect((self.host, self.port))
        return s

    def _send(self, json_packet):
        # Send some JSON to the server.
        
        # TODO check socket not dead.
        # Check if json_packet is already of type string:
        if type(json_packet) == str:
            send_str = json_packet
        else:
            send_str = self._fromJSON(json_packet)

        self.s.send(send_str)

    def _send_and_receive(self, json_packet):
        # General function for sending some JSON
        # Returns a JSON struct of the response
        if (False):
            # If socket is dead, get a new connection
            print("Socket is dead, reconnecting! \n\n")
            self.s = self._startConnection()

        # Check if json_packet is already of type string:
        if type(json_packet) == str:
            send_str = json_packet
        else:
            send_str = self._fromJSON(json_packet)

        self.s.send(send_str)
        resp = self.s.recv(1024)

        # TODO want to return actual JSON
        return resp

        
    def _readlines(self, recv_buffer=4096, delim='\n', lines_to_read=10):
        # Reads the buffer and returns *at least* line_to_read
        buffer = ''
        data = True
        lines = []
        count_idx = 0
        while data:
            data = self.s.recv(recv_buffer)
            buffer += data

            while buffer.find(delim) != -1:
                line, buffer = buffer.split('\n', 1)
                count_idx += 1
                lines.append(line)
                
            if count_idx >= lines_to_read:
                # save input to somewhere., self.blah
                # TODO FIX ME.
                return lines
            
        return
    

    def _close_connection(self):
        self.s.close()
