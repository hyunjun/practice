#   https://leetcode.com/problems/minimum-size-subarray-sum
#   82.96%


class Solution:
    def minSubArrayLen(self, s, nums):
        if nums is None or 0 == len(nums):
            return 0

        start_idx, cur_sum, min_len = 0, 0, 0
        for i in range(len(nums)):
            cur_sum += nums[i]
            if s <= cur_sum:
                if min_len == 0:
                    min_len = i - start_idx + 1
                while s < cur_sum and start_idx < i:
                    cur_sum -= nums[start_idx]
                    start_idx += 1
                    if s <= cur_sum:
                        min_len = min(min_len, i - start_idx + 1)
        return min_len


solution = Solution()
cases = [([2, 3, 1, 2, 4, 3], 7, 2), ([8, 8, 8], 7, 1), ([1, 1, 1], 7, 0), ([1, 2, 3, 4, 5], 11, 3)]
for nums, s, expected in cases:
    real = solution.minSubArrayLen(s, nums)
    print('{}, {}\texpected {}\treal {}\tresult {}'.format(nums, s, expected, real, expected == real))
