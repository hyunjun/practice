import re

if __name__ == '__main__':
  cnt, N = 0, int(raw_input())
  p = re.compile('[H|h]{1}[A|a]{1}[C|c]{1}[K|k]{1}[E|e]{1}[R|r]{2}[A|a]{1}[N|n]{1}[K|k]{1}')
  for i in range(N):
    m = re.search(p, raw_input())
    if m is None:
      continue
    cnt += 1
  print cnt
