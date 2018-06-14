#   https://leetcode.com/problems/balanced-binary-tree
#   77.61%


from TreeNode import TreeNode


class Solution:
    def isBalanced(self, root):
        if root is None:
            return True
        _, result = self.maxDepthRecur(root)
        return result

    def maxDepthRecur(self, node):
        if node is None:
            return 0, True
        lDepth, lResult = self.maxDepthRecur(node.left)
        rDepth, rResult = self.maxDepthRecur(node.right)
        return max(lDepth, rDepth) + 1, abs(lDepth - rDepth) <= 1 and lResult and rResult


s = Solution()

root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
print(s.isBalanced(root))

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(2)
root.left.left = TreeNode(3)
root.left.right = TreeNode(3)
root.left.left.left = TreeNode(4)
root.left.left.right = TreeNode(4)
print(s.isBalanced(root))

root = TreeNode(1)
root.left = TreeNode(2)
root.left.left = TreeNode(3)
root.left.left.left = TreeNode(4)
root.right = TreeNode(2)
root.right.right = TreeNode(3)
root.right.right.right = TreeNode(4)
print(s.isBalanced(root))
