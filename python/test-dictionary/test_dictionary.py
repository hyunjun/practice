#!/usr/bin/env python
#-*- coding: utf8 -*-

import operator
import json
import re
import time
import sys
from collections import defaultdict, Counter
from itertools import ifilter, izip, chain


# control group
from timeit import timeit


def count0(lists) :
  d = dict()
  for l in lists :
    for i in l :
      if i in d :
        d[i] += 1
      else :
        d[i] = 1

  # remove value 1
  for k in d.keys() :
    if d[k] == 1 :
      del d[k]

  return d


def count1(lists) :
  d = {}
  for l in lists :
    for i in l :
      if i in d :
        d[i] += 1
      else :
        d[i] = 1

  for k in d.keys() :
    if d[k] == 1 :
      del d[k]

  return d


def count2(lists) :
  d = defaultdict(lambda: 0)
  for l in lists :
    for i in l :
      d[i] += 1

  for k in d.keys() :
    if d[k] == 1 :
      del d[k]

  return d


def count3(lists) :
  d = defaultdict(int)
  for l in lists :
    for i in l :
      d[i] += 1

  for k in d.keys() :
    if d[k] == 1 :
      del d[k]

  return d


'''
def print_inter_item( inter_item ) :
  for idx, cnt in inter_item.items() :
    key = str(idx) + '-' + str(cnt)
    print key

# https://github.daumkakao.com/pin-park/test_intersection
# https://partofthething.com/thoughts/?p=513
# http://www.markhneedham.com/blog/2015/03/23/python-equivalent-to-flatmap-for-flattening-an-array-of-arrays/
# http://stackoverflow.com/questions/8995611/removing-multiple-keys-from-a-dictionary-safely

def counts7(lists):
  # d = defaultdict(lambda: 0)
  d = defaultdict(int)
  for l in lists:
    for i in sorted(l):
      d[i] += 1
  # return filter(lambda t: t[1] > 1, d.items())
  for k, v in d.copy().iteritems():
    if v == 1:
      # del d[k]
      d.pop(k, None)
  return d

def counts2(lists):
  d = defaultdict(lambda: 0)
  for l in lists:
    for k, v in Counter(l).items():
      d[k] += v
  return ifilter(lambda t: t[1] > 1, d.items())

MAX_ID = 2300000
result = [0] * MAX_ID
def counts3(lists):
  for l in lists:
    for i in l:
      result[i] += 1
  return dict(ifilter(lambda t: t[1] > 1, izip(range(MAX_ID), result)))

def counts4(lists):
  l = lists[0]
  for i in range(1, len(lists)):
    l.extend(lists[i])
  return filter(lambda t: t[1] > 1, Counter(sorted(l)).items())

def counts5(lists):
  d = {}
  for i in chain.from_iterable(lists):
    if i in d:
      d[i] += 1
    else:
      d[i] = 1
  for k, v in d.items():
    if v == 1:
      del d[k]
  return d

def counts6(d6, inp):
  NUM_PATTERN = re.compile('\d+')
  for i in NUM_PATTERN.findall(inp):
    i = int(i)
    if i in d6:
      d6[i] += 1
    else:
      d6[i] = 1
  for k, v in d6.items():
    if v == 1:
      del d6[k]
  return d6
'''

if __name__ == '__main__':
  inp = sys.stdin.readline()
  lists = json.loads(inp)

  for f in [count0, count1, count2, count3]:
    # s = time.time()
    # f(lists)
    # e = time.time()
    # print '{}\t{}'.format(f.__name__, e - s)
    print f.__name__, timeit("{}(lists)".format(f.__name__), setup="from __main__ import {}, lists".format(f.__name__))
  '''
  inp = sys.stdin.readline()
  d6 = dict(izip(range(MAX_ID), [0] * MAX_ID))
  s = time.time()
  r0 = counts6(d6, inp)
  print time.time() - s
  lists = json.loads(inp)
  times = []
  times.append(time.time())
  r1 = count0(lists)
  times.append(time.time())
  r2 = counts7(lists)
  times.append(time.time())
  r3 = counts2(lists)
  times.append(time.time())
  r4 = counts3(lists)
  times.append(time.time())
  r5 = counts4(lists)
  times.append(time.time())
  r6 = counts5(lists)
  times.append(time.time())
  for i in range(1, len(times)):
    print times[i] - times[i - 1]
  #print r1
  #print r2
  #print r3
  #print r4
  #print r5
  #print r6
  '''
