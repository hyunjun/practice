#   https://leetcode.com/problems/contains-duplicate
#   95.38%

#   https://leetcode.com/problems/contains-duplicate/solution


class Solution:
    def containsDuplicate(self, nums):
        s = set()
        for n in nums:
            if n in s:
                return True
            s.add(n)
        return False


s = Solution()
data = [([1,2,3,1], True),
        ([1,2,3,4], False),
        ([1,1,1,3,3,4,3,2,4,2], True)
        ]
for nums, expected in data:
    real = s.containsDuplicate(nums)
    print('{}, expected {}, real {}, result {}'.format(nums, expected, real, expected == real))
