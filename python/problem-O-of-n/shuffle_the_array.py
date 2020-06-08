#   https://leetcode.com/problems/shuffle-the-array


from typing import List


class Solution:
    #   runtime; 108ms, 26.48%
    #   memory; 14.2MB, 100.00%
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        if not (1 <= n <= 500) or nums is None or len(nums) != 2 * n:
            return []
        res = []
        for i in range(n):
            res.append(nums[i])
            res.append(nums[i + n])
        return res


s = Solution()
data = [([2,5,1,3,4,7], 3, [2,3,5,4,1,7]),
        ([1,2,3,4,4,3,2,1], 4, [1,4,2,3,3,2,4,1]),
        ([1,1,2,2], 2, [1,2,1,2]),
        ]
for nums, n, expect in data:
    real = s.shuffle(nums, n)
    print(f'{nums} {n} expect {expect} real {real} result {expect == real}')
