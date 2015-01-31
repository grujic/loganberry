import socket
import json

class ExchangeConnection:
	# Main class for interacting with the exchange

	def __init__(self, host='10.0.129.254', port=25000):
		self.host = host
		self.port = port
		self.s = self._startConnection()
	
	def addOrder(self, stock_ticker, order_id, dir, price, size):
		# Add an order
		json_struct = { \
			"type": "add", \
			"order_id": order_id, \
			"symbol": stock_ticker, \
			"dir": dir, \
			"price": price, \
			"size": size \
		}

		resp = self._send_and_receive(json_struct)

		print(resp)

		return resp

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

		resp = self._send_and_receive(ehlo)

		print resp

		return resp

	### Lower level communications ###
	def _fromJSON(self, json_struct):
		return json.dumps(json_struct) + '\n'

	def _startConnection(self):
		# Open a socket connection
		s = socket.socket()
		s.connect((self.host, self.port))
		return s

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

		return json.loads(resp)

	def _close_connection(self):
		self.s.close()