#!/some/other/python_installed_directory/bin/python
#-*- coding: utf8 -*-
import sys
import networkx
sys.path.append('.')
import external

for line in sys.stdin:
  for word in line.strip().split():
    #print '{}\t{}'.format(word, external.NUMBER)
    print '%s\t%s' % (word, external.NUMBER)
