# https://www.youtube.com/watch?v=sn0DWI-JdNA


class Solution:
  # acc; just for debugging
  def makeChangeRecur(self, total, acc, coins):
    if 0 == len(coins):
      return 0
    if total == 0:
      return 1
    elif total < 0:
      return 0
    ret = 0
    for i, c in enumerate(coins):
      if total < c:
        continue
      acc.append(c)
      ret += self.makeChangeRecur(total - c, acc, coins[i:])
      #print(f'{total - c} {coins[i:]}\t{ret}')
      acc.pop()
    return ret

  def makeChange(self, total, coins):
    return self.makeChangeRecur(total, [], coins)


data = [(16, [10, 6, 4, 2]), (27, [25, 10, 5, 1]), (79, [50, 25, 10, 5, 1])]
s = Solution()
for total, coins in data:
  real = s.makeChange(total, coins)
  print(f'{total}, {coins}, result {real}')
