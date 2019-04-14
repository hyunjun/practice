#   https://leetcode.com/problems/divisor-game

#   https://leetcode.com/problems/divisor-game/discuss/274727/Python-DP


class Solution:
    #   runtime; 36ms, 100.00%
    #   memory; 13.2MB, 100.00%
    def divisorGame(self, N):
        if N % 2 == 0:
            return True
        return False
