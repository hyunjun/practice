#   https://leetcode.com/problems/minimum-absolute-difference-in-bst


from TreeNode import TreeNode
import sys


class Solution:
    #   41.03%
    def getMinimumDifference(self, root):
        vals, stack, cur = [], [], root
        while stack or cur:
            if cur:
                stack.append(cur)
                cur = cur.left
            else:
                cur = stack.pop()
                if cur:
                    vals.append(cur.val)
                cur = cur.right
        minDiff = sys.maxsize
        for i in range(1, len(vals)):
            diff = abs(vals[i - 1] - vals[i])
            if diff < minDiff:
                minDiff = diff
        return minDiff


s = Solution()

root = TreeNode(1)
root.right = TreeNode(3)
root.right.left = TreeNode(2)
print(s.getMinimumDifference(root))
