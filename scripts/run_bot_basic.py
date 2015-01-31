from lib import defs

ec = defs.ExchangeConnection()
ec.sayHello()

for x in xrange(10):
    print 'Iteration {}'.format(x)
    ec.update()