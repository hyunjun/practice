# https://leetcode.com/problems/powx-n/
# https: // en.wikipedia.org / wiki / Addition - chain_exponentiation
# https://www.quora.com/What-are-some-fast-algorithms-for-computing-the-nth-power-of-a-number
import math


class Solution(object):
  def myPow(self, x, n):
    """
    :type x: float
    :type n: int
    :rtype: float
    """
    if x == 0:
      return 0
    if n == 0:
      return 1
    if n == 1:
      return x

    negative = False
    if n < 0:
      negative = True

    if negative:
      n = -n + 1

    result, memoized, cur_x, cur_n = 1, {1: x}, x, 1
    while cur_n < n:
      cur_x = memoized[cur_n] * memoized[cur_n]
      cur_n *= 2
      memoized[cur_n] = cur_x
    cur_n /= 2
    result *= memoized[cur_n]
    #print('memoized {}'.format(memoized))
    rest_n, power_of_two = n - cur_n, 2
    while power_of_two <= rest_n:
      power_of_two *= 2
    power_of_two /= 2
    while 1 < power_of_two:
      #print('rest of n {}\tpower of two {}'.format(rest_n, power_of_two))
      if power_of_two <= rest_n:
        rest_n -= power_of_two
        result *= memoized[power_of_two]
      power_of_two /= 2
    if rest_n == 1:
      result *= x

    if negative:
      return x / result
    return result


solution = Solution()
for x, n in [(0, 10), (10, 0), (2.13457, 1), (2.1, 7), (2.1, -7), (0.00001, 2147483647), (-13.62608, 3)]:
  expected = math.pow(x, n)
  real = solution.myPow(x, n)
  print('x = {}, n = {}\tmath.pow = {}\tmyPow = {}\tresult = {}'.format(x, n, expected, real, expected == real))
