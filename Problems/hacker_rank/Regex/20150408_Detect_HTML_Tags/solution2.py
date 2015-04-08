import re

if __name__ == '__main__':
  p1, p2, N, s = re.compile('<\s*[/]?(\w+)[^<>]*[/]?>'), re.compile('\[.+\]\(http://.+\)'), int(raw_input()), set()
  for i in range(N):
    inp = raw_input()
    m = re.findall(p1, inp)
    [s.add(matched) for matched in m]
    m = re.findall(p2, inp)
    if 0 < len(m):
      s.add('a')
  print ';'.join(sorted(s))
