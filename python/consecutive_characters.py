#   https://leetcode.com/problems/consecutive-characters


from collections import Counter
from collections import defaultdict


class Solution:
    #   runtime; 56ms, 25.00%
    #   memory; 13.9MB, 100.00%
    def maxPower0(self, s: str) -> int:
        if s is None or not (1 <= len(s) <= 500):
            return 0
        stack, maxLen = [], 1
        for c in s:
            if 0 < len(stack) and stack[-1] != c:
                maxLen = max(maxLen, len(stack))
                stack.clear()
            stack.append(c)
        maxLen = max(maxLen, len(stack))
        return maxLen

    #   runtime; 56ms, 25.00%
    #   memory; 13.9MB, 100.00%
    def maxPower(self, s: str) -> int:
        if s is None or not (1 <= len(s) <= 500):
            return 0
        sIdx, maxCnt = 0, 1
        for i, c in enumerate(s):
            if c != s[i - 1]:
                maxCnt = max(maxCnt, i - sIdx)
                sIdx = i
        maxCnt = max(maxCnt, len(s) - sIdx)
        return maxCnt


solution = Solution()
data = [("leetcode", 2),
        ("abbcccddddeeeeedcba", 5),
        ("triplepillooooow", 5),
        ("hooraaaaaaaaaaay", 11),
        ("tourist", 1),
        ("abbcbbbddcc", 3),
        ]
for s, expected in data:
    real = solution.maxPower(s)
    print(f'{s} expected {expected} real {real} result {expected == real}')
