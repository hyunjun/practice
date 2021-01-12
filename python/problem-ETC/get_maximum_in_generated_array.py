#   https://leetcode.com/problems/get-maximum-in-generated-array


class Solution:
    #   runtime; 32ms, 58.79%
    #   memory; 14.2MB, 34.05%
    def getMaximumGenerated(self, n: int) -> int:
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


s = Solution()
data = [(7, 3),
        (2, 1),
        (3, 2),
        (99, 21),
        ]
for n, expect in data:
    real = s.getMaximumGenerated(n)
    print(f'{n} expect {expect} real {real} result {expect == real}')
