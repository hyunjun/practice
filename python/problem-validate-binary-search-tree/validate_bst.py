#   https://leetcode.com/problems/validate-binary-search-tree
#   51.98%


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True

        cur, stack, values = root, [], []
        while cur is not None or 0 < len(stack):
            if cur is not None:
                stack.append(cur)
                cur = cur.left
            else:
                cur = stack.pop()
                values.append(cur.val)
                cur = cur.right
        for i in range(1, len(values)):
            if values[i - 1] >= values[i]:
                return False
        return True


s = Solution()

root = TreeNode(2)
root.left = TreeNode(1)
root.right = TreeNode(3)
print(s.isValidBST(root))

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
print(s.isValidBST(root))

root = TreeNode(5)
root.left = TreeNode(3)
root.left.left = TreeNode(1)
root.left.right = TreeNode(4)
root.right = TreeNode(7)
root.right.right = TreeNode(9)
root.right.right.left = TreeNode(8)
print(s.isValidBST(root))

root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(15)
root.right.left = TreeNode(6)
root.right.right = TreeNode(20)
print(s.isValidBST(root))
