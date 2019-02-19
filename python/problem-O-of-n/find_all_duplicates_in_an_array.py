#   https://leetcode.com/problems/find-all-duplicates-in-an-array


class Solution:
    #   runtime; 168ms, 78,59%
    #   memory; 19.9MB, 100.00%
    def findDuplicates(self, nums):
        if nums is None or 0 == len(nums):
            return []
        s, res = set(), []
        for n in nums:
            if n in s:
                res.append(n)
            else:
                s.add(n)
        return res


s = Solution()
data = [([4, 3, 2, 7, 8, 2, 3, 1], [2, 3]), 
        ]
for nums, expected in data:
    real = s.findDuplicates(nums)
    print('{}, expected {}, real {}, result {}'.format(nums, expected, real, expected == real))
