#   https://leetcode.com/problems/maximum-difference-between-node-and-ancestor


from TreeNode import TreeNode

class Solution:
    #   runtime; 44ms, 100.00%
    #   memory; 14MB, 100.00%
    def maxAncestorDiff(self, root):
        if root is None:
            return 0
        q, maxDiff = [(root.val, root.val, root)], -float('inf')
        while q:
            curMin, curMax, n = q.pop(0)
            maxDiff = max(maxDiff, abs(n.val - curMin), abs(n.val - curMax))
            nextMin, nextMax = min(curMin, n.val), max(curMax, n.val)
            if n.left:
                q.append((nextMin, nextMax, n.left))
            if n.right:
                q.append((nextMin, nextMax, n.right))
        return maxDiff


s = Solution()
root = TreeNode(8)
root.left = TreeNode(3)
root.right = TreeNode(10)
root.left.left = TreeNode(1)
root.left.right = TreeNode(6)
root.right.right = TreeNode(14)
root.left.right.left = TreeNode(4)
root.left.right.right = TreeNode(7)
root.right.right.left = TreeNode(13)
print(s.maxAncestorDiff(root) == 7)
