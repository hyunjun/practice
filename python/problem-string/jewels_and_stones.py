# https://leetcode.com/problems/jewels-and-stones


from collections import Counter


class Solution:
    #   runtime; 76ms
    def numJewelsInStones(self, J, S):
        if J is None or 0 == len(J) or S is None or 0 == len(S):
            return 0

        s, countS = 0, Counter(S)
        for j in J:
            s += countS[j]
        return s

    #   https://leetcode.com/explore/featured/card/may-leetcoding-challenge/534/week-1-may-1st-may-7th/3317
    #   runtime; 20ms, 98.29%
    #   memory; 14MB
    def numJewelsInStones(self, J: str, S: str) -> int:
        if J is None or 0 == len(J) or S is None or 0 == len(S):
            return 0
        stones = Counter(S)
        return sum(stones[j] for j in J)


s = Solution()
data = [("aA", "aAAbbbb", 3), ("z", "ZZ", 0)]
for J, S, expected in data:
    real = s.numJewelsInStones(J, S)
    print(f'{J}, {S}, expected {expected}, real {real}, result {expected == real}')
