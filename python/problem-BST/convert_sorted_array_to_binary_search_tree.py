#   https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree
#   98.35%


from TreeNode import TreeNode


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
