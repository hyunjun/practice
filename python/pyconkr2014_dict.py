# -*- coding: utf8 -*-


# pyconkr2014 http://www.youtube.com/watch?v=E4bF3tPxeDE

'''
# Part I
# 만들기
print {'jan': 1, 'feb': 2, 'mar': 3}
print dict(jan=1, feb=2, mar=3)
month_names = [('jan', 1), ('feb', 2), ('mar', 3), ('apr', 4), ('may', 5), ('jun', 6)]
months = dict(month_names)
print months

print {name.title(): num for name, num in month_names}
print {name: num for name, num in month_names if num % 2 == 0}

print {v: k for k, v in months.items()}

print months['jan']
# print months['Jan']
print 'Jan' in months
print months.get('Jan')
print months.get('Jan', 1)
print months.setdefault('Jan', 1)
print months['Jan']
del months['Jan']
print months.get('Jan')

# 순회
print months.keys()
print [month for month in months]
print months.values()
print months.items()
for m in months.iterkeys():
  print m,
print
for m in months.itervalues():
  print m,
print
for k, v in months.iteritems():
  print '(%s, %d)' % (k, v),
print

words = open('/usr/share/dict/words').read().splitlines()


def lengthDistribution(words):
  length_count = {}
  for l in map(len, words):
    if l in length_count:
      length_count[l] += 1
    else:
      length_count[l] = 1
  return length_count
print lengthDistribution(words)


def lengthDistribution2(words):
  length_count = {}
  for l in map(len, words):
    length_count[l] = length_count.get(l, 0) + 1
  return length_count
print lengthDistribution2(words)


def lenWordDictWrong(words):
  by_len = {}
  for w in words:
    by_len.get(len(w), []).append(w)
  return by_len
print lenWordDictWrong(words)


def lenWordDict(words):
  by_len = {}
  for w in words:
    by_len.setdefault(len(w), []).append(w)
  return by_len
print lenWordDict(words)
'''

'''
# Part II
a = {'jan': 1, 'apr': 4}
b = {'apr': 4, 'jan': 1}
print a == b, a.items() == b.items()

a = {0: 'hello', 1: 'world'}
b = {0: 'hello', 1: 'world'}
for i in xrange(5):
  b[i + 1] = i + 1
for i in xrange(5):
  del b[i + 1]
print a == b, a.items() == b.items()

months = {'jan': 1, 'feb': 2, 'mar': 3, 'apr': 4, 'may': 5, 'jun': 6, 'jul': 7}
# for k, v in months.iteritems(): # RuntimeError
for k, v in months.items():  # ok because items() copys contents
  if 6 <= v:
    del months[k]
print months


class User(object):
  def __init__(self, name, email):
    self.name, self.email = name, email

jongman = User('jongman', 'jongman@gmail.com')
rating = {jongman: 'good'}
print rating[jongman]
jongman2 = User('jongman', 'jongman@gmail.com')
print rating[jongman2]  # KeyError

# __hash__(self): 해시값 반환
# __eq__(self, other): 두 값이 같은지 반환(충돌 해결에 사용). 멤버 변수들이 모두 같으면 같은 값


class User(object):
  def __init__(self, name, email):
    self.name, self.email = name, email

  def members(self):
    return self.name, self.email

  def __eq__(self, other):
    return self.members() == other.members()

  def __hash__(self):
    return hash(self.members())
'''

# Part 3
from collections import OrderedDict
d = OrderedDict()
d['girls'] = 1
d['generation'] = 2
d['gggg'] = 3
d['babybaby'] = 4
print d.items()
d = OrderedDict(girls=1, generation=2, gggg=3, babybaby=4)  # No
print d.items()

from collections import defaultdict
# by_len = defaultdict(lambda: [])  # NOT default value, DEFAULT FUNCTION which returns default value / same effect with setdefault
by_len = defaultdict(list)  # same as above
words = open('/usr/share/dict/words').read().splitlines()
for w in words:
  by_len[len(w)].append(w)
print by_len
# nested defaultdict
A = defaultdict(lambda: defaultdict(list))
for w in words:
  A[len(w)][w[0]].append(w)
print A[4]['h']
# infinite defaultdicts
infinite_dict = lambda: defaultdict(infinite_dict)
inf = infinite_dict()
inf['Users'][0]['username'] = 'jongman'
inf['Users'][0]['email'] = 'jongman@gmail.com'
print inf.items()

from collections import Counter
length_count = Counter(map(len, words))
print length_count[1], length_count[2], length_count[3]
print length_count[1237812]
print length_count.most_common(3)

from shelve import open
shelf = open('test')
shelf['hello'] = 1  # only string key possible
shelf['world'] = 2
shelf.close()  # before close(), not saved

shelf = open('test')
print shelf.items()

from contextlib import closing
with closing(open('a.shelf')) as shelf:
  shelf['hello'] = 1
  shelf['hello'] = 2