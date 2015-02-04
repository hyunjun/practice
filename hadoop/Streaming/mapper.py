#!/usr/bin/env python
#-*- coding: utf8 -*-
import sys
sys.path.append('.')
import external

for line in sys.stdin:
  for word in line.strip().split():
    #print '{}\t{}'.format(word, external.NUMBER)
    print '%s\t%s' % (word, external.NUMBER)
