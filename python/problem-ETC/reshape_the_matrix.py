#   https://leetcode.com/problems/reshape-the-matrix

#   https://leetcode.com/problems/reshape-the-matrix/solution


class Solution:
    #   94.13%, 7min
    def matrixReshape(self, nums, r, c):
        if nums is None or 0 == len(nums) or nums[0] is None or 0 == len(nums[0]):
            return nums
        if len(nums) * len(nums[0]) != r * c:
            return nums
        reshaped = []
        [reshaped.append([None] * c) for i in range(r)]
        rr, cc = 0, 0
        for i in range(len(nums)):
            for j in range(len(nums[0])):
                reshaped[rr][cc] = nums[i][j]
                cc += 1
                if c == cc:
                    rr += 1
                    cc = 0
        return reshaped


s = Solution()
data = [([[1, 2], [3, 4]], 1, 4, [[1, 2, 3, 4]]),
        ([[1, 2], [3, 4]], 2, 4, [[1, 2], [3, 4]]),
        ]
for nums, r, c, expected in data:
    real = s.matrixReshape(nums, r, c)
    print('{}, {}, {}, expected {}, real {}, result {}'.format(nums, r, c, expected, real, expected == real))
