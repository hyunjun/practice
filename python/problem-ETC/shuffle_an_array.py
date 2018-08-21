#   https://leetcode.com/problems/shuffle-an-array

#   https://leetcode.com/problems/shuffle-an-array/solution


import random


#   Time Limit Exceeded
class Solution0:
    def __init__(self, nums):
        self.nums = nums

    def reset(self):
        return self.nums

    def shuffle(self):
        indices, visited = [None] * len(self.nums), set()
        for i, n in enumerate(self.nums):
            newIdx = random.randint(0, len(self.nums) - 1)
            while newIdx in visited or i == newIdx:
                newIdx = random.randint(0, len(self.nums) - 1)
            indices[i] = self.nums[newIdx]
            visited.add(newIdx)
        return indices


#   13.07%
class Solution:
    def __init__(self, nums):
        self.nums = nums

    def reset(self):
        return self.nums

    def shuffle(self):
        lenNums = len(self.nums)
        vals, indices = [None] * lenNums, [i for i in range(lenNums)]
        for i, n in enumerate(self.nums):
            newIdx = indices[random.randint(0, len(indices) - 1)]
            vals[i] = self.nums[newIdx]
            indices.remove(newIdx)
        return vals


s = Solution([1, 2, 3])
print(s.shuffle())
print(s.reset())
