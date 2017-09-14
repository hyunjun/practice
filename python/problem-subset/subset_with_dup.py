#   https://leetcode.com/problems/subsets-ii
#   18.42%

import math

class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if nums is None or 0 == len(nums):
            return [[]]
        if 1 == len(nums):
            return [[], nums]
        nums.sort() #   처음에 이걸 빠뜨림
        result, cnt_subsets = [[]], int(math.pow(2, len(nums)))
        for i in range(1, cnt_subsets):
            bit_check, idx, temp = i, 0, []
            while 0 < bit_check:
                if bit_check & 0x1:
                    temp.append(nums[idx])
                bit_check >>= 1
                idx += 1
            if temp in result:
                continue
            result.append(temp)
        return result

s = Solution()
print(s.subsetsWithDup([1, 2, 2]))
print(s.subsetsWithDup([1, 2, 3]))
print(s.subsetsWithDup([4,4,4,1,4]))
