#   https://leetcode.com/problems/flip-equivalent-binary-trees

#   https://leetcode.com/problems/flip-equivalent-binary-trees/solution


from TreeNode import TreeNode

class Solution:
    #   runtime; 36ms, 99.81%
    #   memory; 12.4MB, 0.84%
    def flipEquiv(self, root1, root2):

        def isFlipEq(node1, node2):
            if node1 is None and node2 is None:
                return True
            if node1 is None or node2 is None or node1.val != node2.val:
                return False
            return (isFlipEq(node1.left, node2.left) and isFlipEq(node1.right, node2.right)) or (isFlipEq(node1.left, node2.right) and isFlipEq(node1.right, node2.left))

        return isFlipEq(root1, root2)


s = Solution()
root1 = TreeNode(1)
root1.left = TreeNode(2)
root1.right = TreeNode(3)
root1.left.left = TreeNode(4)
root1.left.right = TreeNode(5)
root1.right.left = TreeNode(6)
root1.left.right.left = TreeNode(7)
root1.left.right.right = TreeNode(8)
root2 = TreeNode(1)
root2.left = TreeNode(3)
root2.right = TreeNode(2)
root2.left.right = TreeNode(6)
root2.right.left = TreeNode(4)
root2.right.right = TreeNode(5)
root2.right.right.left = TreeNode(8)
root2.right.right.right = TreeNode(7)
print(s.flipEquiv(root1, root2))
