#   http://www.grantjenks.com/docs/sortedcontainers/
from sortedcontainers import SortedList
sl = SortedList(['e', 'a', 'c', 'd', 'b'])
print(sl)
sl *= 10000000
print(sl.count('c'))
print(sl[-3:])
['e', 'e', 'e']

from sortedcontainers import SortedDict
sd = SortedDict({'c': 3, 'a': 1, 'b': 2})
print(sd)
SortedDict({'a': 1, 'b': 2, 'c': 3})
print(sd.popitem())

from sortedcontainers import SortedSet
ss = SortedSet('abracadabra')
print(ss)
print(ss.bisect_left('c'))
