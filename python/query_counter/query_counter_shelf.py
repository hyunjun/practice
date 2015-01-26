# -*- coding: utf-8 -*-
from contextlib import closing
import shelve
import datetime
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

  with closing(shelve.open('qc.shelf')) as shelf:
    if cmd == 'input':
      print 'input query count from ', inp
      idx = get_index(inp)
      lines = open(inp).read().splitlines()
      for l in lines:
        q, c = l.split('\t')
        if q in shelf:
          ar = shelf[q]
        else:
          ar = [0] * 256
        ar[idx] = c
        shelf[q] = ar
    else: # get query count
      idx = get_index(cmd)
      print '{} -> {}'.format(cmd, idx)
      if inp in shelf:
        print inp, shelf[inp][idx]
