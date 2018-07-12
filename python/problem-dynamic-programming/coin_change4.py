#   https://www.youtube.com/watch?v=tduLvFbqRXE


class Solution:
  def coinChange(self, coins, amount):
    dp = [0] * (amount + 1)
    dp[0] = 1
    for c in coins:
      for a in range(amount + 1):
        if a < c:
          continue
        dp[a] += dp[a - c]
      print(dp)
    return dp[-1]


print(Solution().coinChange([1, 2, 3], 5))
