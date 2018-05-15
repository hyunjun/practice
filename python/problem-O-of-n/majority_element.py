#   https://leetcode.com/problems/majority-element
#   91.20%

#   https://leetcode.com/problems/majority-element/solution


from collections import Counter


class Solution:
        def majorityElement(self, nums):
            minCount = len(nums) // 2
            counter = Counter(nums)
            majorityNum, majorityCount = nums[0], counter[nums[0]]
            for k, v in counter.items():
                if minCount < v and majorityCount < v:
                    majorityNum, majorityCount = k, v
            return majorityNum


s = Solution()
data = [([3, 2, 3], 3), ([2, 2, 1, 1, 1, 2, 2], 2)]
for nums, expect in data:
    real = s.majorityElement(nums)
    print('{}, expect {}, real {}, result {}'.format(nums, expect, real, expect == real))
