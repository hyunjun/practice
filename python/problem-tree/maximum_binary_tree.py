#   https://leetcode.com/problems/maximum-binary-tree

#   https://leetcode.com/problems/maximum-binary-tree/solution


from TreeNode import TreeNode


class Solution:
    #   51.19%
    def constructMaximumBinaryTree(self, nums):
        if nums is None or 0 == len(nums):
            return None
        if 1 == len(nums):
            return TreeNode(nums[0])
        def maximumBinaryTree(arr):
            if arr is None or 0 == len(arr):
                return None
            maxVal, maxIdx = arr[0], 0
            for i, a in enumerate(arr):
                if maxVal < a:
                    maxVal, maxIdx = a, i
            node = TreeNode(maxVal)
            node.left = maximumBinaryTree(arr[:maxIdx])
            node.right = maximumBinaryTree(arr[maxIdx + 1:])
            return node
        return maximumBinaryTree(nums)


s = Solution()
nums = [3, 2, 1, 6, 0, 5]
'''
      6
    /   \
   3     5
    \    /
     2  0
       \
        1
'''
print(s.constructMaximumBinaryTree(nums))
