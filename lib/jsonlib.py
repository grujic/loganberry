import json
import socket


def request(exchange_ip='10.0.129.254',
            port=25000,
            send_str,
            team_string='LOGANBERRY'):
    
    """
    
    """
    
    s = socket.socket()
    s.connect((host, port))
    
    ehlo = {"type": "hello",
            "team": team_string}
    hello_str = json.dumps(ehlo) + '\n'
    
    # send hello string
    s.send(hello_str)
    resp = s.recv(1024)  # bad, ignore return for now.
    
    # send command string
    s.send(send_str)
    resp = s.recv(1024)  
    s.close()
    
    return resp
   