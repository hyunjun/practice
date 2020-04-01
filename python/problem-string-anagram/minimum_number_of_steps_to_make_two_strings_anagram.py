#   https://leetcode.com/problems/minimum-number-of-steps-to-make-two-strings-anagram


from collections import defaultdict


class Solution:
    #   runtime; 500ms, 5.02%
    #   memory; 15.1MB, 100.00%
    def minSteps0(self, s: str, t: str) -> int:
        if s is None or t is None or not (1 <= len(s) <= 50000) or not (1 <= len(t) <= 50000) or len(s) != len(t):
            return -1
        ss, st = sorted(s), sorted(t)
        if ss == st:
            return 0
        d = {chr(i): 0 for i in range(97, 97 + 26)}
        for c in s:
            d[c] += 1
        for c in t:
            d[c] -= 1
        return sum(i for i in d.values() if i > 0)

    #   runtime; 248ms, 37.31%
    #   memory; 14.4MB, 100.00%
    def minSteps1(self, s: str, t: str) -> int:
        if s is None or t is None or not (1 <= len(s) <= 50000) or not (1 <= len(t) <= 50000) or len(s) != len(t):
            return -1
        d = {chr(i): 0 for i in range(97, 97 + 26)}
        for c in s:
            d[c] += 1
        for c in t:
            d[c] -= 1
        return sum(i for i in d.values() if i > 0)

    #   runtime; 176ms, 55.24%
    #   memory; 14.3MB, 100.00%
    def minSteps(self, s: str, t: str) -> int:
        if s is None or t is None or not (1 <= len(s) <= 50000) or not (1 <= len(t) <= 50000) or len(s) != len(t):
            return -1
        d = defaultdict(int)
        for c in s:
            d[c] += 1
        for c in t:
            d[c] -= 1
        return sum(i for i in d.values() if i > 0)


solution = Solution()
data = [('bab', 'aba', 1),
        ('leetcode', 'practice', 5),
        ('anagram', 'mangaar', 0),
        ('xxyyzz', 'xxyyzz', 0),
        ('friend', 'family', 4),
        ]
for s, t, expected in data:
    real = solution.minSteps(s, t)
    print(f'{s} {t} expected {expected} real {real} result {expected == real}')
