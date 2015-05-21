import re

if __name__ == '__main__':
  p, N = re.compile('[a-z]{0,3}\d{2,8}[A-Z]{3,}'), int(raw_input())
  for i in range(N):
    m = re.match(p, raw_input())
    if m is None:
      print 'INVALID'
    else:
      print 'VALID'
