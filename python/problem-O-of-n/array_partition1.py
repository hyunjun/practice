#   https://leetcode.com/problems/array-partition-i

#   https://leetcode.com/problems/array-partition-i/discuss/155731/Two-Lines-Python-Solution-Easy-to-Understand


class Solution:
    #   0.0%
    def arrayPairSum(self, nums):
        d = {i: 0 for i in range(-10000, 10001)}
        for n in nums:
            d[n] += 1
        res = []
        for i in range(-10000, 10001):
            if 0 < d[i]:
                [res.append(i) for j in range(d[i])]
        return sum([r for i, r in enumerate(res) if 0 == i % 2])


s = Solution()
data = [([1, 4, 3, 2], 4),
        ]
for nums, expected in data:
    real = s.arrayPairSum(nums)
    print('{}, expected {}, real {}, result {}'.format(nums, expected, real, expected == real))
