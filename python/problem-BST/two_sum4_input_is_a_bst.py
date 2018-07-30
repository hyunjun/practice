#   https://leetcode.com/problems/two-sum-iv-input-is-a-bst

#   https://leetcode.com/problems/two-sum-iv-input-is-a-bst/solution


from TreeNode import TreeNode


class Solution:
    #   28.01%
    def findTarget(self, root, k):
        if root is None:
            return False
        cur, stack, res = root, [], []
        while cur or stack:
            if cur:
                stack.append(cur)
                cur = cur.left
            else:
                cur = stack.pop()
                res.append(cur.val)
                cur = cur.right
        l, r = 0, len(res) - 1
        while l < r:
            curSum = res[l] + res[r]
            if k == curSum:
                return True
            elif k < curSum:
                r -= 1
            else:
                l += 1
        return False


s = Solution()

root = TreeNode(5)
root.left = TreeNode(3)
root.left.left = TreeNode(2)
root.left.right = TreeNode(4)
root.right = TreeNode(6)
root.right.right = TreeNode(7)
print(s.findTarget(root, 9))
print(s.findTarget(root, 28))
