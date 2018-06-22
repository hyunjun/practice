# https://leetcode.com/problems/sqrtx


class Solution:
  def mySqrt(self, x):
    if x == 0 or x == 1:
      return x
    if x == 2 or x == 3:
      return 1

    for i in range(2, x // 2 + 1):
      if i * i == x:
        return i
      if x < i * i:
        return i - 1
    return i

class Solution2:
  def mySqrt(self, x):
    # newton's method
    r = x
    while r * r > x:
      r = (r + x / r) / 2
    return r



s, s2 = Solution(), Solution2()
for x in [2, 3, 4, 9, 8, 5, 15, 98, 10000092, 2147395599]:
  expected, real = s2.mySqrt(x), s.mySqrt(x)
  print('{}\texpected {}\treal {}\tresult {}'.format(x, expected, real, expected == real))