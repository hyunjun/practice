

from typing import List


class Solution:
    def getSumRecur(self, nums: List[int], n: int) -> bool:
        if nums is None or 0 == len(nums):
            return False

        def _getSum(acc, arr):
            if acc == n:
                return True
            for i, a in enumerate(arr):
                acc += a
                subRes = _getSum(acc, arr[:i] + arr[i + 1:])
                if subRes:
                    return True
                acc -= a
            return False

        return _getSum(0, nums)


s = Solution()
data = [([3, 2, 7, 1], 6, True),
        ([3, 2, 7, 0], 6, False),
        ]
for nums, n, expected in data:
    real = s.getSumRecur(nums, n)
    print(f'{nums} {n} expected {expected} real {real} result {expected == real}')
