import socket
import json

class ExchangeConnection:
	# Main class for interacting with the exchange

	def __init__(self, host='10.0.129.254', port=25000):
		self.host = host
		self.port = port

	def addOrder(self):
		# Add an order
		pass

	def convertOrder(self):
		# Convert an ETH to its components
		pass

	def cancelOrder(self):
		# Cancel an order
		pass

	def sayHello(self):
		# Check connection
		### TEMP ###
		s = self._startConnection()
		
		ehlo = {"type": "hello", "team": "LOGANBERRY"}

		send_str = self._fromJSON(ehlo)

		s.send(send_str)
		resp = s.recv(1024)
		s.close()

		print resp

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
		s = self._startConnection()

		# Check if json_packet is already of type string:
		if type(json_packet) == str:
			send_str = json_packet
		else:
			send_str = self._fromJSON(json_packet)

		s.send(send_str)
		resp = s.recv(1024)
		s.close()

		return json.loads(resp)