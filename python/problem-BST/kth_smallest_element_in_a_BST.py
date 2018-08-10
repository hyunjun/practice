#   https://leetcode.com/problems/kth-smallest-element-in-a-bst


from TreeNode import TreeNode


#   45.15%
class Solution:
    def kthSmallest0(self, root, k):
        cur, stack, res = root, [], []
        while cur or stack:
            if cur:
                stack.append(cur)
                cur = cur.left
            else:
                cur = stack.pop()
                res.append(cur.val)
                cur = cur.right
        return res[k - 1]

    def kthSmallest(self, root, k):
        cur, stack = root, []
        while cur or stack:
            if cur:
                stack.append(cur)
                cur = cur.left
            else:
                cur = stack.pop()
                k -= 1
                if 0 == k:
                    return cur.val
                cur = cur.right
        return -1


s = Solution()

root1 = TreeNode(3)
root1.left = TreeNode(1)
root1.left.right = TreeNode(2)
root1.right = TreeNode(4)
print(s.kthSmallest(root1, 1))

root2 = TreeNode(5)
root2.left = TreeNode(3)
root2.left.left = TreeNode(2)
root2.left.left.left = TreeNode(1)
root2.left.right = TreeNode(4)
root2.right = TreeNode(6)
print(s.kthSmallest(root2, 3))
