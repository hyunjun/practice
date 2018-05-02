#   https://leetcode.com/problems/symmetric-tree


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSymmetric(self, root):
        if root is None:
            return True
        return self.isSymmetricRecur(root.left, root.right)

    #   100.00%
    def isSymmetricRecur(self, lNode, rNode):
        if lNode is None and rNode is None:
            return True
        if lNode is None or rNode is None:
            return False
        if lNode.val != rNode.val:
            return False
        return self.isSymmetricRecur(lNode.left, rNode.right) and self.isSymmetricRecur(lNode.right, rNode.left)



s = Solution()

r = TreeNode(1)
r.left = TreeNode(2)
r.right = TreeNode(2)
r.left.left = TreeNode(3)
r.left.left.left = TreeNode(5)
r.left.right = TreeNode(4)
r.right.left = TreeNode(4)
r.right.right = TreeNode(3)
r.right.right.right = TreeNode(5)
print(s.isSymmetric(r))

r = TreeNode(1)
r.left = TreeNode(2)
r.right = TreeNode(2)
r.left.right = TreeNode(3)
r.right.right = TreeNode(3)
print(s.isSymmetric(r))

r = TreeNode(1)
r.left = TreeNode(2)
r.right = TreeNode(3)
r.left.left = TreeNode(3)
r.right.left = TreeNode(2)
print(s.isSymmetric(r))

r = TreeNode(1)
r.left = TreeNode(2)
r.right = TreeNode(2)
r.left.left = TreeNode(3)
r.left.left.right = TreeNode(5)
r.left.right = TreeNode(4)
r.right.left = TreeNode(4)
r.right.right = TreeNode(3)
r.right.right.right = TreeNode(5)
print(s.isSymmetric(r))
