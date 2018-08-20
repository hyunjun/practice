#   https://leetcode.com/problems/wiggle-subsequence

#   https://leetcode.com/problems/wiggle-subsequence/solution


class Solution:
    #   85.64%
    def wiggleMaxLength(self, nums):
        if nums is None or 0 == len(nums):
            return 0
        if 1 == len(nums):
            return 1
        wiggle = [None] * len(nums)
        for i, n in enumerate(nums):
            if 0 == i:
                continue
            if nums[i - 1] < n:
                wiggle[i] = True
            elif nums[i - 1] > n:
                wiggle[i] = False
        prev, cnt = None, 1
        for i in range(1, len(wiggle)):
            if 1 == i:
                if wiggle[i] is not None:
                    cnt += 1
                    prev = wiggle[i]
                continue
            if wiggle[i] is not None:
                if prev is None or prev != wiggle[i]:
                    prev = wiggle[i]
                    cnt += 1
        return cnt


s = Solution()
data = [([1, 7, 4, 9, 2, 5], 6),
        ([1, 17, 5, 10, 13, 15, 10, 5, 16, 8], 7),
        ([1, 2, 3, 4, 5, 6, 7, 8, 9], 2),
        ([], 0),
        ([1], 1),
        ([0, 0], 1),
        ]
for nums, expected in data:
    real = s.wiggleMaxLength(nums)
    print('{}, expected {}, real {}, result {}'.format(nums, expected, real, expected == real))
