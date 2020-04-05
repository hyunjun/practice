#   https://www.geeksforgeeks.org/length-of-the-longest-substring-without-repeating-characters


class Solution:
    def longestSubNoRepeat(self, s):
        if s is None or 0 == len(s):
            return 0
        if 1 == len(s):
            return 1
        d, si, ei, m = {}, 0, 0, 1
        for i, c in enumerate(s):
            if c not in d:
                d[c] = -1
            if d[c] >= 0:
                si = max(si, d[c] + 1)
            ei = d[c] = i
            m = max(m, ei - si + 1)
        return m


solution = Solution()
data = [('ABDEFGABEF', 6),
        ('BBBB', 1),
        ('GEEKSFORGEEKS', 7),
        ]
for s, expected in data:
    real = solution.longestSubNoRepeat(s)
    print(f'{s} expected {expected} real {real} result {expected == real}')
