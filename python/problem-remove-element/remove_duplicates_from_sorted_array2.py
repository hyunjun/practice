#   https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/description/


class Solution(object):
    #   86.55%
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums is None or 0 == len(nums):
            return 0
        if 1 == len(nums):
            return 1

        totalLen = len(nums)
        i, j = 0, 0
        jCnt, noneCnt = 0, 0
        while j < totalLen:
            if nums[i] == nums[j]:
                jCnt += 1
                if 3 <= jCnt:
                    nums[j] = None
                    noneCnt += 1
            else:
                i = j
                jCnt = 1
            j += 1
        while 0 < noneCnt:
            nums.remove(None)
            noneCnt -= 1
        return len(nums)
        '''
        noneIdx, idx = 0, 0
        while noneIdx < totalLen and idx < totalLen:
            while noneIdx < totalLen and nums[noneIdx] is not None:
                noneIdx += 1
            idx = noneIdx + 1
            while idx < totalLen and nums[idx] is None:
                idx += 1
            if noneIdx < totalLen and idx < totalLen:
                nums[noneIdx], nums[idx] = nums[idx], nums[noneIdx]
            noneIdx += 1
        noneIdx = len(nums) - 1
        while nums[noneIdx] is None:
            noneIdx -= 1
        return noneIdx + 1
        '''

    #   https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/discuss/126376/Python-simple-Two-Pointers-solution-(beats-99)
    def removeDuplicates0(self, nums):
        if not nums:
            return 0
        i = 0
        for j in range(1, len(nums)):
            if nums[i] != nums[j] or (0 < i and nums[i] != nums[i - 1]) or 0 == i:
                i += 1
                nums[i] = nums[j]
        return i + 1

s = Solution()
data = [([1], 1),
        ([1, 2, 3], 3),
        ([1, 1, 1, 2, 2, 3], 5),
        ([0, 0, 1, 1, 2, 2, 3], 7),
        ([1, 1, 1, 2, 2, 2, 3, 3, 3, 4], 7)
       ]
for nums, expected in data:
  real = s.removeDuplicates(nums)
  print('nums {}\texpected {}\treal {}\tresult {}'.format(nums, expected, real, expected == real))
