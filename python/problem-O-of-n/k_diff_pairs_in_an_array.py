#   https://leetcode.com/problems/k-diff-pairs-in-an-array


class Solution:
    #   27.78%
    def findPairs(self, nums, k):
        if nums is None or 0 == len(nums) or k < 0:
            return 0

        d, resSet = {}, set()
        for n in nums:
            if n in d:
                d[n] += 1
            else:
                d[n] = 1

        for n, cnt in d.items():
            if 0 == k:
                if 1 < cnt:
                    resSet.add((n, n))
            else:
                if n - k in d:
                    smaller, bigger = min(n - k, n), max(n - k, n)
                    resSet.add((smaller, bigger))
                if n + k in d:
                    smaller, bigger = min(n, n + k), max(n, n + k)
                    resSet.add((smaller, bigger))

        return len(resSet)


s = Solution()
data = [([3, 1, 4, 1, 5], 2, 2),
        ([1, 2, 3, 4, 5], 1, 4),
        ([1, 3, 1, 5, 4], 0, 1),
        ([1, 2, 3, 4, 5], -1, 0),
        ]
for nums, k, expected in data:
    real = s.findPairs(nums, k)
    print('{}, {}, expected {}, real {}, result {}'.format(nums, k, expected, real, expected == real))
