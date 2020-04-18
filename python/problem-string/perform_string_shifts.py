#   https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/529/week-2/3299


from typing import List


class Solution:
    #   runtime; 32ms
    #   memory; 13.9MB
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        if s is None or not (1 <= len(s) <= 100) or shift is None or not (1 <= len(shift) <= 100):
            return s
        for direction, amount in shift:
            if len(s) < amount:
                amount %= len(s)
            if direction == 0:
                s = s[amount:] + s[:amount]
            else:
                moveIdx = len(s) - amount
                s = s[moveIdx:] + s[:moveIdx]
        return s


solution = Solution()
data = [('abc', [[0, 1], [1, 2]], 'cab'),
        ('abcdefg', [[1, 1], [1, 1], [0, 2], [1, 3]], 'efgabcd'),
        ]
for s, shift, expected in data:
    real = solution.stringShift(s, shift)
    print(f'{s} {shift} expected {expected} real {real} result {expected == real}')
