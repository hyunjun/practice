# https://www.youtube.com/watch?v=jaNZ83Q3QGc


class Solution:
  def coinChange(self, coins, amount):
    dp = [amount + 1] * (amount + 1)
    dp[0] = 0
    for a in range(amount + 1):
      for c in coins:
        if a < c:
          continue
        dp[a] = min(dp[a], dp[a - c] + 1)
    if amount < dp[-1]:
      return -1
    print(dp)
    return dp[-1]


print(Solution().coinChange([1, 2, 5], 12))
print(Solution().coinChange([2], 3))
print(Solution().coinChange([3, 4], 7))
