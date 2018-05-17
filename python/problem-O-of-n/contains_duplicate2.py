#   https://leetcode.com/problems/contains-duplicate-ii
#   91.97%

#   https://leetcode.com/problems/contains-duplicate-ii/discuss/130445/Simple-O(n)-time-and-O(n)-space-Python-Solution


class Solution:
    def containsNearbyDuplicate(self, nums, k):
        if nums is None or len(nums) <= 1 or 0 == k:
            return False
        s = set()
        for i in range(k + 1):
            if i < len(nums):
                if nums[i] in s:
                    return True
                s.add(nums[i])
        for i in range(k + 1, len(nums)):
            s.remove(nums[i - k - 1])
            if nums[i] in s:
                return True
            s.add(nums[i])
        return False


s = Solution()
data = [([1,2,3,1], 3, True),
        ([1,2,3,4], 3, False),
        ([1,1,3,4], 3, True),
        ([1,0,1,1], 1, True),
        ([1,2,1], 0, False),
        ([1], 1, False),
        ([99, 99], 2, True),
        ([2, 2], 3, True),
        ([1, 2], 2, False),
        ]
for nums, k, expected in data:
    real = s.containsNearbyDuplicate(nums, k)
    print('{}, expected {}, real {}, result {}'.format(nums, expected, real, expected == real))
