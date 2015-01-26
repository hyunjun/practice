# -*- coding: utf-8 -*-
from contextlib import closing
import pickle
import datetime
import os
import re
import sys


START_DATE = datetime.date(2014, 6, 1)


DATE_PATTERN = re.compile('\d{8}', re.U)
def get_date(s):
  m = re.search(DATE_PATTERN, s)
  if m is not None:
    date_str = m.group()
    return datetime.date(int(date_str[:4]), int(date_str[4:6]), int(date_str[6:]))
  return None


def get_index(s):
  return (get_date(s) - START_DATE).days


if __name__ == '__main__':
  if len(sys.argv) < 3:
    sys.exit(1)

  cmd, inp = sys.argv[1], ' '.join(sys.argv[2:])
  print cmd, inp

  dict = {}
  if os.path.isfile('qc.dict'):
    dict = pickle.load(open('qc.dict', 'rb'))

  if cmd == 'input':
    print 'input query count from ', inp
    idx = get_index(inp)
    lines = open(inp).read().splitlines()
    for l in lines:
      q, c = l.split('\t')
      q = hash(q)
      if q in dict:
        ar = dict[q]
      else:
        ar = [0] * 256
      ar[idx] = c
      dict[q] = ar
    pickle.dump(dict, open('qc.dict', 'wb'))
  else: # get query count
    idx = get_index(cmd)
    print '{} -> {}'.format(cmd, idx)
    if inp in dict:
      print inp, dict[hash(inp)][idx]
