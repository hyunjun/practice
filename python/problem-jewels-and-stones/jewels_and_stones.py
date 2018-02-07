# https://leetcode.com/problems/jewels-and-stones
# data 부족으로 %는 안 나옴
from collections import Counter


class Solution:
  def numJewelsInStones(self, J, S):
    if J is None or 0 == len(J) or S is None or 0 == len(S):
      return 0

    s, countS = 0, Counter(S)
    for j in J:
      s += countS[j]
    return s


s = Solution()
data = [("aA", "aAAbbbb", 3), ("z", "ZZ", 0)]
for J, S, expected in data:
  real = s.numJewelsInStones(J, S)
  print(f'{J}, {S}, expected {expected}, real {real}, result {expected == real}')
