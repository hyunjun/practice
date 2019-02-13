#   https://leetcode.com/problems/binary-tree-pruning

#   https://leetcode.com/problems/binary-tree-pruning/solution


from TreeNode import TreeNode

class Solution:
    #   runtime; 32ms, 100.00%
    #   memory; 12.7MB, 0.55%
    def pruneTree(self, root):

        def areAllZeroes(node):
            if node is None:
                return None
            node.left, node.right = areAllZeroes(node.left), areAllZeroes(node.right)
            if node.left is None and node.right is None and 0 == node.val:
                return None
            return node

        return areAllZeroes(root)


s = Solution()

root1 = TreeNode(1)
root1.right = TreeNode(0)
root1.right.left = TreeNode(0)
root1.right.right = TreeNode(1)
print(s.pruneTree(root1))

root2 = TreeNode(1)
root2.left = TreeNode(0)
root2.right = TreeNode(1)
root2.left.left = TreeNode(0)
root2.left.right = TreeNode(0)
root2.right.left = TreeNode(0)
root2.right.right = TreeNode(1)
print(s.pruneTree(root2))

root3 = TreeNode(1)
root3.left = TreeNode(1)
root3.right = TreeNode(0)
root3.left.left = TreeNode(1)
root3.left.right = TreeNode(1)
root3.right.left = TreeNode(0)
root3.right.right = TreeNode(1)
root3.left.left.left = TreeNode(0)
print(s.pruneTree(root3))
