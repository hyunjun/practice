#   https://leetcode.com/problems/subarray-product-less-than-k

#   https://leetcode.com/problems/subarray-product-less-than-k/solution


class Solution(object):
    #   8.85%
    def numSubarrayProductLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if k <= 0:
            return 0
        def foo(n):
            if 0 < n:
                return n * (n + 1) // 2
            return 0
        s, e, p, res = 0, 0, 1, []
        while s < len(nums) and e < len(nums):
            p *=nums[e]
            if k <= p:
                res.append((s, e))
                while s < len(nums) and k <= p:
                    p //= nums[s]
                    s += 1
            e += 1
        res.append((s, e))
        s, e, _sum = 0, 0, 0
        while s < len(res) and e < len(res):
            _sum += foo(res[e][1] - res[s][0])
            s += 1
            if s < len(res) and res[e][1] > res[s][0]:
                _sum -= foo(res[e][1] - res[s][0])
            e += 1
        return _sum


s = Solution()
data = [([10, 5, 2, 6], 100, 8),
        ([1, 2, 3], 0, 0),
        ([1, 1, 1], 1, 0),
        ([10, 9, 10, 4, 3, 8, 3, 3, 6, 2, 10, 10, 9, 3], 19, 18),
        ]
for nums, k, expected in data:
    real = s.numSubarrayProductLessThanK(nums, k)
    print('{}, {}, expected {}, real {}, result {}'.format(nums, k, expected, real, expected == real))
