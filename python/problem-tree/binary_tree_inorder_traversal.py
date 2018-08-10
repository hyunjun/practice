#   https://leetcode.com/problems/binary-tree-inorder-traversal

#   https://leetcode.com/problems/binary-tree-inorder-traversal/solution


from TreeNode import TreeNode


class Solution:
    #   98.99%
    def inorderTraversal(self, root):
        cur, stack, res = root, [], []
        while cur or stack:
            if cur:
                stack.append(cur)
                cur = cur.left
            else:
                cur = stack.pop()
                res.append(cur.val)
                cur = cur.right
        return res


s = Solution()
root = TreeNode(1)
root.right = TreeNode(2)
root.right.left = TreeNode(3)
print(s.inorderTraversal(root))
