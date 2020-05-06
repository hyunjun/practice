#   https://leetcode.com/problems/majority-element

#   https://leetcode.com/problems/majority-element/solution


from collections import Counter


class Solution:
    #   runtime; 52ms, 91.20%
    def majorityElement0(self, nums):
        minCount = len(nums) // 2
        counter = Counter(nums)
        majorityNum, majorityCount = nums[0], counter[nums[0]]
        for k, v in counter.items():
            if minCount < v and majorityCount < v:
                majorityNum, majorityCount = k, v
        return majorityNum

    #   https://leetcode.com/explore/featured/card/may-leetcoding-challenge/534/week-1-may-1st-may-7th/3321
    #   runtime; 164ms, 95.36%
    #   memory; 15.4MB
    def majorityElement(self, nums: List[int]) -> int:
        return sorted(Counter(nums).items(), key=lambda t: -t[1])[0][0]


s = Solution()
data = [([3, 2, 3], 3), ([2, 2, 1, 1, 1, 2, 2], 2)]
for nums, expect in data:
    real = s.majorityElement(nums)
    print('{}, expect {}, real {}, result {}'.format(nums, expect, real, expect == real))
