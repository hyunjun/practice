#!/usr/bin/env python
#-*- coding: utf8 -*-

import sys

if __name__ == '__main__':
  while 1:
    try:
      line = sys.stdin.readline()
    except KeyboardInterrupt:
      break
    if not line:
      break
    line = line.strip()
    if line == "" : continue
    id, n_in, n_out, r_in, r_out = line.split()
    print '%s\t%f\t%f' % (id, int(n_in.replace(',', '')) - int(n_out.replace(',', '')), float(r_in) - float(r_out))
