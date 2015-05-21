import re

if __name__ == '__main__':
  strs, subs, N, cnt = [], [], int(raw_input()), 0
  [strs.append(raw_input()) for i in range(N)]
  T = int(raw_input())
  [subs.append(re.compile('[a-zA-Z0-9_]{1}%s[a-zA-Z0-9_]{1}' % raw_input())) for i in range(T)]
  for p in subs:
    cnt = 0
    for s in strs:
      m = re.findall(p, s)
      cnt += len(m)
    print cnt
