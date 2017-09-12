#   https://leetcode.com/problems/subsets

class Solution(object):
    def subsetsRecur(self, nums):
        if 1 == len(nums):
            return [[], nums]
        s = []
        for i in range(len(nums)):
            temp = nums[:i]
            temp.extend(nums[i + 1:])
            s.extend(self.subsetsRecur(temp))
        s.append(nums)
        return s

    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if nums is None or 0 == len(nums):
            return [[]]
        result = []

        #   list에 set을 사용하면 TypeError: unhashable type: 'list' 발생
        for elem in self.subsetsRecur(nums):
            if elem in result:
                continue
            result.append(elem)
        return result


s = Solution()
print(s.subsets([]))
print(s.subsets([1]))
print(s.subsets([1, 2]))
print(s.subsets([1, 2, 3]))
print(s.subsets([1,2,3,4,5,6,7,8,10,0]))    #   Time Limit Exceeded
