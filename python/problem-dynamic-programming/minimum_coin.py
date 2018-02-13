# https://www.youtube.com/watch?v=PPgGJvgv2Ag
# https://github.com/codingcasserole/MinimumCoinDPSolution/blob/master/main.cpp
# https://docs.google.com/spreadsheets/d/12lzDu-TO6vdc1m_A6yjOnhzVCNQGbDCMsdT0qIcXesE/edit?usp=sharing


class Solution:
  def minimumCoin(self, coins, target):
    if coins is None or 0 == len(coins):
      return 0

    dp = [target + 1] * (target + 1)
    dp[0] = 0
    print(dp)
    for i in range(1, target + 1):
      print(f'[{i}] {dp}')
      for c in coins:
        if i < c:
          continue
        dp[i] = min(dp[i], dp[i - c] + 1)
    print(dp)
    if target < dp[-1]:
      return -1
    return dp[-1]

    
coins = [1, 2, 3, 5]
target = 9
print(Solution().minimumCoin(coins, target))
