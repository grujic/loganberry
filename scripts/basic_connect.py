import socket
import json

exchange_ip = 'http://10.0.129.254'
ehlo = {"type": "hello", "team": "LOGANBERRY"}

#resp = requests.post(exchange_ip,
                     #port=25000,
                     #data=ehlo)

host = '10.0.129.254'
port = 25000

send_str = json.dumps(ehlo) + '\n'

s = socket.socket()
s.connect((host, port))
s.send(send_str)
resp = s.recv(1024)
s.close()

print resp