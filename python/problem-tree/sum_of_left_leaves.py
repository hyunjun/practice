#   https://leetcode.com/problems/sum-of-left-leaves
#   25.21%

#   https://leetcode.com/problems/sum-of-left-leaves/discuss/133053/Python-5-line-Simple-recursive-solution


from TreeNode import TreeNode


class Solution:
    def sumOfLeftLeaves(self, root):
        if root is None:
            return 0
        queue, res = [(root, False)], 0
        while queue:
            cur, isLeft = queue[0]
            del queue[0]
            if isLeft and cur.left is None and cur.right is None:
                res += cur.val
            if cur.left:
                queue.append((cur.left, True))
            if cur.right:
                queue.append((cur.right, False))
        return res


s = Solution()

'''
    3
   / \
  9  20
    /  \
   15   7
'''
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
print(root)
print(s.sumOfLeftLeaves(root))
