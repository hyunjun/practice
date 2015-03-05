s = 'string'
print '{}\t{}'.format(s, isinstance(s, str))
us = u'unicode'
print '{}\t{}'.format(us, isinstance(us, unicode))
num = 3
print '{}\t{}'.format(num, isinstance(num, int))
floating_num = 3.0
print '{}\t{}'.format(floating_num, isinstance(floating_num, float))

# https://docs.python.org/2/library/collections.html
import collections
l = [1, 2, 3]
print '{}\t{}'.format(l, isinstance(l, collections.MutableSequence))
s = {1, 1, 2, 3}
print '{}\t{}'.format(s, isinstance(s, collections.MutableSet))
d = {'a':'1', 'b':'2', 'c':'3'}
print '{}\t{}'.format(d, isinstance(d, collections.MutableMapping))
