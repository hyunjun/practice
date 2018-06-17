#   https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array
#   5.68%

#   https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/discuss/137453/2-lines-python-AC-code-beats-99


class Solution:
    def findDisappearedNumbers(self, nums):
        if nums is None or 0 == len(nums):
            return []
        for i, n in enumerate(nums):
            tmp = nums[i]
            while i + 1 != tmp and nums[i] != nums[tmp - 1]:
                nums[i], nums[tmp - 1] = nums[tmp - 1], nums[i]
                tmp = nums[i]
        res = []
        for i, n in enumerate(nums):
            if i + 1 != n:
                res.append(i + 1)
        return res


s = Solution()
data = [([4, 3, 2, 7, 8, 2, 3, 1], [5, 6])]
for nums, expected in data:
    real = s.findDisappearedNumbers(nums)
    print('{}, expected {}, real {}, result {}'.format(nums, expected, real, expected == real))
'''
    0 1 2 3 4 5 6 7
i   4 3 2 7 8 2 3 1
0   7     4
    3           7
    2   3
    3 2              nums[i] == nums[nums[i] - 1]
1     2              nums[i] == i + 1
2
3
4           1     8
    1       3        nums[i] == nums[nums[i] - 1]
5             2
6               7
7                 8
'''
