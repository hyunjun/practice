#   https://leetcode.com/problems/reformat-the-string


class Solution:
    #   runtime; 48ms, 87.21%
    #   memory; 14MB, 100.00%
    def reformat(self, s: str) -> str:
        if not (1 <= len(s) <= 500):
            return ''
        chs, nums = [c for c in s if 'a' <= c <= 'z'], [c for c in s if '0' <= c <= '9']
        bigger, smaller = chs, nums
        if len(bigger) < len(smaller):
            bigger, smaller = smaller, bigger
        if len(bigger) == len(smaller) or len(bigger) == len(smaller) + 1:
            return ''.join([bigger[i // 2] if i % 2 == 0 else smaller[i // 2] for i in range(len(s))])
        return ''


solution = Solution()
data = [('a0b1c2', 'a0b1c2'),
        ('leetcode', ''),
        ('1229857369', ''),
        ('covid2019', 'c2o0v1i9d'),
        ('ab123', '1a2b3'),
        ]
for s, expected in data:
    real = solution.reformat(s)
    print(f'{s} expected {expected} real {real} result {expected == real}')
