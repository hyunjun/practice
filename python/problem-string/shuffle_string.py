#   https://leetcode.com/problems/shuffle-string


from typing import List


class Solution:
    #   runtime; 56ms, 92.47%
    #   memory; 14.1MB, 100.00%
    def restoreString(self, s: str, indices: List[int]) -> str:
        if s is None or 0 == len(s) or indices is None or 0 == len(indices) or len(s) != len(indices):
            return ''
        d = {indices[i]: c for i, c in enumerate(s)}
        return ''.join(c for _, c in sorted(d.items()))


solution = Solution()
data = [("codeleet", [4,5,6,7,0,2,1,3], "leetcode"),
        ("abc", [0,1,2], "abc"),
        ("aiohn", [3,1,4,2,0], "nihao"),
        ("aaiougrt", [4,0,2,6,7,3,1,5], "arigatou"),
        ("art", [1,0,2], "rat"),
        ]
for s, indices, expect in data:
    real = solution.restoreString(s, indices)
    print(f'{s} {indices} expect {expect} real {real} result {expect == real}')
