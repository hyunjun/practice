#   https://leetcode.com/problems/invert-binary-tree

#   https://leetcode.com/problems/invert-binary-tree/solution


from TreeNode import TreeNode


class Solution:

    #   44.59% O(n), O(n)
    def invertTree(self, root):
        if root is None:
            return None
        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        return root


'''
     4
   /   \
  2     7
 / \   / \
1   3 6   9

     4
   /   \
  7     2
 / \   / \
9   6 3   1
'''
root = TreeNode(4)
root.left = TreeNode(2)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
root.right = TreeNode(7)
root.right.left = TreeNode(6)
root.right.right = TreeNode(9)
print(root)

s = Solution()
print(s.invertTree(root))
