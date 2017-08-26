# https://leetcode.com/problems/excel-sheet-column-title
def bar(n):
  if n <= 0:
    return ''
  base, d, sup = 26, 26, 0
  while base < n:
    d *= 26
    sup += 1
    base += d
  d //= 26
  print('d {}\tsup {}\tn {}'.format(d, sup, n))
  result = []
  while 0 < sup and d < n:
    c = n // d
    if n % d == 0:
      c -= 1
    print('d {}\tn {}\tc {}\t{}'.format(d, n, c, chr(c + 64)))
    result.append(chr(c + 64))
    n -= c * d
    d //= 26
    sup -= 1
  print('d {}\tn {}\t{}'.format(d, n, chr(n + 64)))
  result.append(chr(n + 64))
  return ''.join(result)


import math


def zoo(s):
  res, sup = 0, len(s) - 1
  for c in s:
    n = math.pow(26, sup) * (ord(c) - 64)
    print('{} -> {}'.format(c, math.pow(26, sup) * (ord(c) - 64)))
    sup -= 1
    res += n
  return int(res)


class Solution:
  # @return a string
  def convertToTitle(self, num):
    capitals = [chr(x) for x in range(ord('A'), ord('Z')+1)]
    result = []
    while num > 0:
      result.append(capitals[(num-1)%26])
      num = (num-1) // 26
    result.reverse()
    return ''.join(result)

for n in [1, 26, 27, 676, 701, 1048]:
  # 701 -> ZY
  print('[{}]'.format(n))
  s = bar(n)
  nn = zoo(s)
  print('s {}\tback to n {}\t{}'.format(s, nn, n == nn))
