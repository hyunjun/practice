# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/

class Solution(object):
  def maxProfit(self, prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    if prices is None or 0 == len(prices):
      return 0

    cur_min = cur_max = prices[0]
    result = 0
    for p in prices[1:]:
      if p < cur_min:
        cur_min = cur_max = p
      if cur_max < p:
        cur_max = p
      if result < cur_max - cur_min:
        result = cur_max - cur_min
    return result


s = Solution()
cases = [([7, 1, 5, 3, 6, 4], 5), ([7, 6, 4, 3, 1], 0), ([2, 4, 1], 2)]
for prices, expected in cases:
  real = s.maxProfit(prices)
  print('{}\texpected {}\treal {}\tresult {}'.format(prices, expected, real, expected == real))

