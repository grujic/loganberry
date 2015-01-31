from time import sleep
from lib import defs

ec = defs.ExchangeConnection(port=25001)
ec.sayHello()

for x in xrange(10):
    print 'Iteration {}'.format(x)
    sleep(5)
    ec.update()

print("Book data = ")
print(ec.book.data)