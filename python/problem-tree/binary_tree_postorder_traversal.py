#   https://leetcode.com/problems/binary-tree-postorder-traversal


from TreeNode import TreeNode


class Solution:
    #   98.73%
    def postorderTraversal(self, root):
        if root is None:
            return []
        stack, res = [root], []
        while stack:
            cur = stack.pop()
            res.append(cur.val)
            if cur.left:
                stack.append(cur.left)
            if cur.right:
                stack.append(cur.right)
        return res[::-1]


s = Solution()
'''
    1
   / \
  2   3
 /     \
4       5
4 2 5 3 1
'''
root = TreeNode(1)
root.left = TreeNode(2)
root.left.left = TreeNode(4)
root.right = TreeNode(3)
root.right.right = TreeNode(5)
print(s.postorderTraversal(root))
