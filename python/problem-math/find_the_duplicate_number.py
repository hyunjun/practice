#   https://leetcode.com/problems/find-the-duplicate-number


class Solution:
    #   Wrong Answer
    def findDuplicate0(self, nums):
        maxNum = max(nums)
        return sum(nums) - maxNum * (maxNum + 1) // 2

    #   Wrong Answer
    def findDuplicate1(self, nums):
        minNum, maxNum = min(nums), max(nums)
        if minNum == maxNum:
            return minNum
        if 1 < minNum:
            uniqSum = (maxNum * (maxNum + 1) - (minNum - 1) * minNum) // 2
        else:
            uniqSum = maxNum * (maxNum + 1) // 2
        return (sum(nums) - uniqSum) // (len(nums) - (maxNum - minNum + 1))

    #   Time Limit Exceeded
    def findDuplicate2(self, nums):
        for i, n in enumerate(nums):
            for j in range(i + 1, len(nums)):
                if n == nums[j]:
                    return n
        return -1

    #   https://leetcode.com/problems/find-the-duplicate-number/solution
    def findDuplicate(self, nums):
        tortoise, hare = nums[0], nums[0]
        while True:
            tortoise, hare = nums[tortoise], nums[nums[hare]]
            if tortoise == hare:
                break
        ptr1, ptr2 = nums[0], tortoise
        while ptr1 != ptr2:
            ptr1, ptr2 = nums[ptr1], nums[ptr2]
        return ptr1


s = Solution()
data = [([1, 3, 4, 2, 2], 2),
        ([3, 1, 3, 4, 2], 3),
        ([2, 2, 2, 2, 2], 2),
        ([4, 2, 2, 3, 2], 2),
        ([1, 4, 4, 2, 4], 4),
        ]
for nums, expected in data:
    real = s.findDuplicate(nums)
    print('{}, expected {}, real {}, result {}'.format(nums, expected, real, expected == real))
