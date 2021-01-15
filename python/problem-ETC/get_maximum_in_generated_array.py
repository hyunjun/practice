#   https://leetcode.com/problems/get-maximum-in-generated-array


class Solution:
    #   runtime; 32ms, 58.79%
    #   memory; 14.2MB, 34.05%
    def getMaximumGenerated0(self, n: int) -> int:
        nums = []
        for i in range(n + 1):
            if 0 == i:
                nums.append(0)
            elif 1 == i:
                nums.append(1)
            elif i % 2 == 0:
                nums.append(nums[i // 2])
            else:
                nums.append(nums[i // 2] + nums[i // 2 + 1])
        return max(nums)

    #   https://leetcode.com/explore/challenge/card/january-leetcoding-challenge-2021/581/week-3-january-15th-january-21st/3605
    #   runtime; 28ms, 87.00%
    #   memory; 14.3MB
    def getMaximumGenerated(self, n: int) -> int:
        if n < 0:
            return []
        if n == 0 or n == 1:
            return n
        nums = [0] * (n + 1)
        maxNum = nums[1] = 1
        for i in range(2, n + 1):
            if i % 2 == 0:
                nums[i] = nums[i // 2]
            else:
                nums[i] = nums[i // 2] + nums[i // 2 + 1]
            maxNum = max(maxNum, nums[i])
        return maxNum


s = Solution()
data = [(7, 3),
        (2, 1),
        (3, 2),
        (99, 21),
        ]
for n, expect in data:
    real = s.getMaximumGenerated(n)
    print(f'{n} expect {expect} real {real} result {expect == real}')
