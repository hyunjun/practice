# -*- coding: utf-8 -*-
from contextlib import closing
import redis
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
  return int((get_date(s) - START_DATE).days)


if __name__ == '__main__':
  if len(sys.argv) < 3:
    sys.exit(1)

  cmd, inp = sys.argv[1], ' '.join(sys.argv[2:])
  print cmd, inp

  conn = redis.StrictRedis(host='127.0.0.1', port=6379, db=0)

  if cmd == 'input':
    print 'input query count from ', inp
    idx = get_index(inp)
    print idx, type(idx)
    lines = open(inp).read().splitlines()
    #cur.executemany('insert into qc values (?, ?)', [(hash(l.split('\t')[0]), l.split('\t')[1]) for l in lines])
    init_list = [0] * 256
    for l in lines:
      q, c = l.split('\t')
      if 0 == conn.llen(hash(q)):
        conn.lpush(hash(q), *init_list)
      conn.lset(hash(q), idx, int(c))
    print 'total {} entries'.format(conn.hlen('qc'))
  else: # get query count
    idx = get_index(cmd)
    print '{} -> {}'.format(cmd, idx)
    print inp, '->', conn.lindex(hash(inp), idx)
