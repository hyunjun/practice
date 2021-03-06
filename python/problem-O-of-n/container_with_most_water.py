#   https://leetcode.com/problems/container-with-most-water
#   71.00%


class Solution:

    def maxArea(self, height):
        if height is None or len(height) < 2:
            return 0

        maxSize, l, r = 0, 0, len(height) - 1
        while l < r:
            maxSize = max(maxSize, (r - l) * min(height[l], height[r]))
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return maxSize


data = [([1, 2, 3, 4, 5], 6), ([5, 2, 3, 4, 5], 20), ([1, 1], 1), ([1, 2, 1], 2), ([1, 8, 6, 2, 5, 4, 8, 3, 7], 49)]
s = Solution()
for height, expected in data:
    real = s.maxArea(height)
    print('{}, expected {}, real {}, result {}'.format(height, expected, real, expected == real))
