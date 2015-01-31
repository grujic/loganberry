from time import sleep
from lib import defs

ec = defs.ExchangeConnection(port=25002)
ec.sayHello()

for x in xrange(10):
    print 'Iteration {}'.format(x)
    sleep(1)
    ec.update()
    
    ec.addOrder('QUUX', 'BUY', 1, 50)
    ec.addOrder('QUUX', 'BUY', 10000, 50)

print("Book data = ")
print(ec.book.data)