#   https://leetcode.com/problems/decompress-run-length-encoded-list


from typing import List


class Solution:
    #   runtime; 68ms, 63.48%
    #   memory; 13MB, 100.00%
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        if nums is None or not (2 <= len(nums) <= 100):
            return []
        res = []
        for i in range(1, len(nums), 2):
            [res.append(nums[i]) for _ in range(nums[i - 1])]
        return res


s = Solution()
data = [([1, 2, 3, 4], [2, 4, 4, 4]),
        ]
for nums, expected in data:
    real = s.decompressRLElist(nums)
    print(f'{nums} expected {expected} real {real} result {expected == real}')
