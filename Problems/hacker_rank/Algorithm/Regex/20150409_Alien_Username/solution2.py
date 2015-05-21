import re

if __name__ == '__main__':
  p, N = re.compile('^[_.]{1}\d+[a-zA-Z]*[_]?$'), int(raw_input())
  for i in range(N):
    m = re.match(p, raw_input())
    if m is None:
      print 'INVALID'
    else:
      print 'VALID'
