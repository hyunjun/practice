#   https://leetcode.com/problems/increasing-decreasing-string


from collections import Counter


class Solution:
    #   runtime; 76ms, 40.21%
    #   memory; 12.8MB, 100.00%
    def sortString0(self, s: str) -> str:
        if s is None or not (1 <= len(s) <= 500):
            return ''
        c, result = Counter(s), []
        while len(result) < len(s):
            for i in range(ord('a'), ord('z') + 1):
                ch = chr(i)
                if c[ch] > 0:
                    result.append(ch)
                    c[ch] -= 1
            for i in range(ord('z'), ord('a') - 1, -1):
                ch = chr(i)
                if c[ch] > 0:
                    result.append(ch)
                    c[ch] -= 1
        return ''.join(result)

    #   runtime; 64ms, 70.74%
    #   memory; 13.9MB, 100.00%
    def sortString(self, s: str) -> str:
        if s is None or not (1 <= len(s) <= 500):
            return ''
        c, result = Counter(s), []
        keys = sorted(c.keys())
        while len(result) < len(s):
            for ch in keys:
                if c[ch] > 0:
                    result.append(ch)
                    c[ch] -= 1
            for ch in keys[::-1]:
                if c[ch] > 0:
                    result.append(ch)
                    c[ch] -= 1
        return ''.join(result)


solution = Solution()
data = [('aaaabbbbcccc', 'abccbaabccba'),
        ('rat', 'art'),
        ('leetcode', 'cdelotee'),
        ('ggggggg', 'ggggggg'),
        ('spo', 'ops'),
        ]
for s, expected in data:
    real = solution.sortString(s)
    print(f'{s} expected {expected} real {real} result {expected == real}')
