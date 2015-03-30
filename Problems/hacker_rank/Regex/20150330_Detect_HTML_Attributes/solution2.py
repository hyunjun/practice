from collections import OrderedDict
import re

if __name__ == '__main__':
  p, p_attr_name = re.compile('<(\w+)( \w+=["\']{1}[^<>]+["\']{1})?( /)?>'), re.compile('(\w+)=["\']{1}')
  d, N = {}, int(raw_input())
  for i in range(N):
    doc = raw_input()
    matches = re.findall(p, doc)
    for m in matches:
      tag, attr = m[0], m[1]
      if 0 < len(attr):
        for attr in re.findall(p_attr_name, attr):
          d.setdefault(tag, set()).add(attr)
      else:
        d.setdefault(tag, set())
  for tag, attrs in d.items():
    d[tag] = ','.join(sorted(attrs))
  for tag, attrs in OrderedDict(sorted(d.items())).items():
    print '{}:{}'.format(tag, attrs)
