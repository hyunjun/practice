import re

if __name__ == '__main__':
  p, N = re.compile('hi [^d]', re.I), int(raw_input())
  for i in range(N):
    s = raw_input()
    m = re.match(p, s)
    if m is not None:
      print s
