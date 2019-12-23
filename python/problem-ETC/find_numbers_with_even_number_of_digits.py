#   https://leetcode.com/problems/find-numbers-with-even-number-of-digits


from typing import List


class Solution:
    #   runtime; 44ms, 97.29%
    #   memory; 12.9MB, 100.00%
    def findNumbers(self, nums: List[int]) -> int:
        if nums is None or not (1 <= len(nums) <= 500):
            return 0
        return sum(1 if len(str(num)) % 2 == 0 else 0 for num in nums)


s = Solution()
data = [([12, 345, 2, 6, 7896], 2),
        ([555, 901, 482, 1771], 1),
        ]
for nums, expected in data:
    real = s.findNumbers(nums)
    print(f'{nums} expected {expected} real {real} result {expected == real}')
