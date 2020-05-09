#   https://leetcode.com/problems/check-if-a-string-can-break-another-string


from typing import List


class Solution:
    #   runtime; 140ms, 90.71%
    #   memory; 16MB, 100.00%
    def checkIfCanBreak(self, s1: str, s2: str) -> bool:
        if s1 is None or s2 is None or not (1 <= len(s1) <= 10 ** 5) or not (1 <= len(s2) <= 10 ** 5) or len(s1) != len(s2):
            return False
        s1, s2 = sorted(s1), sorted(s2)
        return all(c >= s2[i] for i, c in enumerate(s1)) or all(c <= s2[i] for i, c in enumerate(s1))


s = Solution()
data = [("abc", "xya", True),
        ("abe", "acd", False),
        ("leetcodee", "interview", True),
        ]
for s1, s2, expected in data:
    real = s.checkIfCanBreak(s1, s2)
    print(f'{s1} {s2} expected {expected} real {real} result {expected == real}')
