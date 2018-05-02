#   https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree
#   98.35%


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __str__(self):
        lVal, rVal = 'x', 'x'
        if self.left is None and self.right is None:
            lVal, rVal = '', ''
        if self.left:
            lVal = self.left
        if self.right:
            rVal = self.right
        return '({} {} {})'.format(lVal, self.val, rVal)


class Solution(object):
    def sortedArrayToBST(self, nums):
        if nums is None or 0 == len(nums):
            return None
        return self.sortedArrayToBSTRecur(nums)

    def sortedArrayToBSTRecur(self, nums):
        if nums is None or 0 == len(nums):
            return None
        mid = len(nums) // 2
        node = TreeNode(nums[mid])
        node.left = self.sortedArrayToBSTRecur(nums[:mid])
        node.right = self.sortedArrayToBSTRecur(nums[mid + 1:])
        return node


nums = [-10, -3, 0, 5, 9]
'''
        _______0______
       /              \
    __-3__          ___9__
   /      \        /      \
 -10       x       5       x
'''
s = Solution()
root = s.sortedArrayToBST(nums)
print(root)
