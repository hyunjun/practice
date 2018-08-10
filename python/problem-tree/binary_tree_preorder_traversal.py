#   https://leetcode.com/problems/binary-tree-preorder-traversal


from TreeNode import TreeNode


class Solution:
    #   98.36%
    def preorderTraversal(self, root):
        if root is None:
            return []
        stack, res = [root], []
        while stack:
            cur = stack.pop()
            res.append(cur.val)
            if cur.right:
                stack.append(cur.right)
            if cur.left:
                stack.append(cur.left)
        return res


s = Solution()
root = TreeNode(1)
root.left = TreeNode(2)
root.left.left = TreeNode(4)
root.right = TreeNode(3)
root.right.right = TreeNode(5)
print(s.preorderTraversal(root))
