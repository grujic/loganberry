import socket
import json

class ExchangeConnection:
	# Main class for interacting with the exchange

	def __init__(self, exchange_address):
		self.exchange_address = exchange_address

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
		exchange_ip = 'http://10.0.129.254'
		ehlo = {"type": "hello", "team": "LOGANBERRY"}

		host = '10.0.129.254'
		port = 25000

		send_str = json.dumps(ehlo) + '\n'

		s = socket.socket()
		s.connect((host, port))
		s.send(send_str)
		resp = s.recv(1024)
		s.close()

		print resp