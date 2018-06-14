#   https://leetcode.com/problems/remove-duplicates-from-sorted-array
#   문제에서는 length를 반환하라고 되어 있지만
#   실제로는 array 앞쪽에 중복 제거된 값들을 모으는 상태로 변형시켜야만 함
#   즉 중복을 제거한 후 개수만 반환하면 통과하지 못함


class Solution(object):

    #   time limit exceeded
    def removeDuplicates0(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums is None or 0 == len(nums):
            return 0

        totalLen = len(nums)
        idx = totalLen - 1
        while 0 < idx:
            if nums[idx - 1] < nums[idx]:
                idx -= 1
                continue
            delNum, delIdx = nums[idx], idx - 1
            while -1 < delIdx and nums[delIdx] == delNum:
                nums[delIdx] = None
                print('del idx {} -> {}'.format(delIdx ,nums))
                delIdx -= 1
            idx = delIdx

        firstNoneIdx, idx = 0, 0
        while firstNoneIdx < totalLen and idx < totalLen:
            while firstNoneIdx < totalLen and nums[firstNoneIdx] is not None:
                firstNoneIdx += 1
            idx = firstNoneIdx + 1
            while idx < totalLen and nums[idx] is None:
                idx += 1
            if firstNoneIdx < totalLen and idx < totalLen:
                nums[firstNoneIdx], nums[idx] = nums[idx], nums[firstNoneIdx]
                firstNoneIdx += 1

        return firstNoneIdx

    #   76.51%
    def removeDuplicates0(self, nums):
        if nums is None or 0 == len(nums):
            return 0

        totalLen = len(nums)
        idx, dupLen = totalLen - 1, 0
        while 0 < idx:
            if nums[idx - 1] < nums[idx]:
                idx -= 1
                continue
            delNum, delIdx = nums[idx], idx - 1
            while -1 < delIdx and nums[delIdx] == delNum:
                nums[delIdx] = None
                dupLen += 1
                print('del idx {} -> {}'.format(delIdx ,nums))
                delIdx -= 1
            idx = delIdx
        dupRemovedLen = totalLen - dupLen
        print(nums, dupRemovedLen)
        idx, dupRemovedIdx = 0, 0
        while idx < totalLen:
            if nums[idx] is not None:
                nums[dupRemovedIdx], nums[idx] = nums[idx], nums[dupRemovedIdx]
                dupRemovedIdx += 1
            idx += 1
        print(nums)
        return dupRemovedLen

    #   45.09%
    def removeDuplicates1(self, nums):
        if nums is None or 0 == len(nums):
            return 0
        lenNums, l, r = len(nums), 0, 1
        while r < lenNums:
            while r < lenNums and nums[r] <= nums[l]:
                r += 1
            if r < lenNums:
                l += 1
                nums[l], nums[r] = nums[r], nums[l]
        print(nums)
        return l + 1

    #   https://leetcode.com/problems/remove-duplicates-from-sorted-array/solution/
    def removeDuplicates(self, nums):
        if nums is None or 0 == len(nums):
            return 0
        i = 0
        for j in range(1, len(nums)):
            if nums[i] != nums[j]:
                i += 1
                nums[i] = nums[j]
        return i + 1


s = Solution()
data = [([1, 1], [1]),
        ([1, 1, 2], [1, 2]),
        ([1, 2, 3], [1, 2, 3]),
        ([0, 0, 1, 1, 1, 2, 2, 3, 3, 4], [0, 1, 2, 3, 4]),
       ]
for nums, expected in data:
  real = s.removeDuplicates(nums)
  print('nums {}\texpected {}\treal {}\tresult {}'.format(nums, expected, real, expected == nums[:real]))
'''
0, 0, 1, 1, 1, 2, 2, 3, 3, 4
l  r
   l  r
0, 1, 0, 1, 1, 2, 2, 3, 3, 4
   l           r
      l        r
0, 1, 2, 1, 1, 0, 2, 3, 3, 4
      l              r
         l           r
0, 1, 2, 3, 1, 0, 2, 1, 3, 4
         l                 r
            l              r
0, 1, 2, 3, 4, 0, 2, 1, 3, 1
'''
