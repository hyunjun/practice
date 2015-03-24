import re

if __name__ == '__main__':
  p = re.compile('(\d{1,3})[- ]{1}(\d{1,3})[- ]{1}(\d{4,10})')
  N = int(raw_input())
  for i in range(N):
    m = re.search(p, raw_input())
    if m is not None:
      print 'CountryCode={},LocalAreaCode={},Number={}'.format(m.group(1), m.group(2), m.group(3))
