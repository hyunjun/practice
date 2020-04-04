#   https://leetcode.com/problems/single-number

#   https://leetcode.com/problems/single-number/solution/


from collections import Counter


class Solution:
    #   95.12%
    def singleNumber0(self, nums):
        for num, count in Counter(nums).items():
            if 1 == count:
                return num
        return None

    #   https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/528/week-1/3283/
    #   without extra space
    #   runtime; 96ms, 23.85%
    #   memory; 16.4MB
    def singleNumber(self, nums: List[int]) -> int:
        if nums is None or 0 == len(nums):
            return None
        if 1 == len(nums):
            return nums[0]
        sortedNums = sorted(nums)
        for i, n in enumerate(sortedNums):
            if 0 == i and n != sortedNums[i + 1]:
                return n
            elif len(sortedNums) - 1 == i and sortedNums[i - 1] != n:
                return n
            elif sortedNums[i - 1] != n and n != sortedNums[i + 1]:
                return n
        return None


s = Solution()
data = [([2, 2, 1], 1), ([4, 1, 2, 1, 2], 4)]
for nums, expected in data:
    real = s.singleNumber(nums)
    print('{}, expected {}, real {}, result {}'.format(nums, expected, real, expected == real))
