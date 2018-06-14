#   https://leetcode.com/problems/path-sum
#   96.19%


from TreeNode import TreeNode


class Solution:
    def hasPathSum(self, root, sum):
        if root is None:
            return False
        queue = [(root, 0)]
        while queue:
            cur, prevSum = queue[0]
            del queue[0]
            if cur.left is None and cur.right is None:
                if prevSum + cur.val == sum:
                    return True
            if cur.left:
                queue.append((cur.left, prevSum + cur.val))
            if cur.right:
                queue.append((cur.right, prevSum + cur.val))
        return False


s = Solution()

root = TreeNode(5)
root.left = TreeNode(4)
root.left.left = TreeNode(11)
root.left.left.left = TreeNode(7)
root.left.left.left = TreeNode(2)
root.right = TreeNode(8)
root.right.left = TreeNode(13)
root.right.right = TreeNode(4)
root.right.right.right = TreeNode(1)
print(s.hasPathSum(root, 22))
