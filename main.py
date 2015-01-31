# Basic imports
import sys

# Our imports
from lib.defs import ExchangeConnection

PUBLIC_EXCHANGE_PUBLIC_IP = "54.154.191.94"
PUBLIC_EXCHANGE_PUBLIC_IP = "10.0.129.254"

exchange_host = sys.argv[1]
port_index = sys.argv[2]


### Read in command line arguments ###
print("\n\n")
print("exchange host address = " + exchange_host + "\n\n")
print("port index = " + port_index + "\n\n")

### Instantiate connection to the exchange ###
conn = ExchangeConnection(PUBLIC_EXCHANGE_PUBLIC_IP)
