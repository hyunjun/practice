#   https://leetcode.com/problems/maximum-average-subarray-i

#   https://leetcode.com/problems/maximum-average-subarray-i/solution

class Solution:
    #   Wrong Answer
    def findMaxAverage0(self, nums, k):
        if nums is None or 0 == len(nums):
            return 0
        kSum, maxAvg = 0, None
        for i, n in enumerate(nums):
            kSum += n
            if k <= i:
                kSum -= nums[i - k]
                print('nums[{}:{}], sum {}, kSum {}, avg {}, kAvg {}'.format(i - k + 1, i + 1, sum(nums[i - k + 1:i + 1]), kSum, sum(nums[i - k + 1:i + 1]) / k, kSum / k))
                avg = kSum / k
                if maxAvg is None or maxAvg < avg:
                    maxAvg = avg
        if maxAvg is None:
            return sum(nums) / k
        return maxAvg

    #   32.25%
    def findMaxAverage(self, nums, k):
        if nums is None or 0 == len(nums):
            return 0
        kSum, maxAvg = 0, None
        for i, n in enumerate(nums):
            kSum += n
            if k - 1 <= i:
                print('nums[{}:{}], sum {}, kSum {}, avg {}, kAvg {}'.format(i - k + 1, i + 1, sum(nums[i - k + 1:i + 1]), kSum, sum(nums[i - k + 1:i + 1]) / k, kSum / k))
                avg = kSum / k
                if maxAvg is None or maxAvg < avg:
                    maxAvg = avg
                kSum -= nums[i - k + 1]
        return maxAvg


s = Solution()
data = [([1, 12, -5, -6, 50, 3], 4, 12.75),
        ([1, 12, -5, -6, 50, 3], 1, 50),
        ([5], 1, 5.0),
        ([-6662, 5432, -8558, -8935, 8731, -3083, 4115, 9931, -4006, -3284, -3024, 1714, -2825, -2374, -2750, -959, 6516, 9356, 8040, -2169, -9490, -3068, 6299, 7823, -9767, 5751, -7897, 6680, -1293, -3486, -6785, 6337, -9158, -4183, 6240, -2846, -2588, -5458, -9576, -1501, -908, -5477, 7596, -8863, -4088, 7922, 8231, -4928, 7636, -3994, -243, -1327, 8425, -3468, -4218, -364, 4257, 5690, 1035, 6217, 8880, 4127, -6299, -1831, 2854, -4498, -6983, -677, 2216, -1938, 3348, 4099, 3591, 9076, 942, 4571, -4200, 7271, -6920, -1886, 662, 7844, 3658, -6562, -2106, -296, -3280, 8909, -8352, -9413, 3513, 1352, -8825], 90, 37.25556),
        ([9, 7, 3, 5, 6, 2, 0, 8, 1, 9], 6, 5.33333),
        ]
for nums, k, expected in data:
    real = s.findMaxAverage(nums, k)
    if 10 < len(nums):
        print('{}...({}), {}, expected {}, real {}, result {}'.format(nums[:10], len(nums), k, expected, real, expected == real))
    else:
        print('{}, {}, expected {}, real {}, result {}'.format(nums, k, expected, real, expected == real))
