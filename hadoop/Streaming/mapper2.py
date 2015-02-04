#!/usr/bin/env python
#-*- coding: utf8 -*-
import re
import sys
sys.path.append('.')
import external

BLANK_PATTERN = re.compile('\s{2,}')
for line in sys.stdin:
  title, description, url, epoch_time = line.strip().split('\t')
  for sentences in [title, description]:
    sentences = re.sub(BLANK_PATTERN, '', sentences).strip()
    if 0 == len(sentences):
      continue
    for word in sentences.split():
      try:
        #print '{}\t{}'.format(word, external.NUMBER)
        print '%s\t%s' % (word, external.NUMBER)
      except ValueError:
        pass
