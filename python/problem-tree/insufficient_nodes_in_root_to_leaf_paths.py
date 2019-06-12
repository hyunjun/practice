#   https://leetcode.com/problems/insufficient-nodes-in-root-to-leaf-paths


from TreeNode import TreeNode


class Solution:
    #   runtime; 92ms, 89.61%
    #   memory; 15MB, 100.00%
    def sufficientSubset(self, root: TreeNode, limit: int) -> TreeNode:
        if root is None:
            return root

        def calc(prevSum, n):
            if n.left is None and n.right is None:
                if prevSum + n.val < limit:
                    return None
                return n

            if n.left:
                n.left = calc(prevSum + n.val, n.left)
            if n.right:
                n.right = calc(prevSum + n.val, n.right)
            if n.left is None and n.right is None:
                return None
            return n

        return calc(0, root)


s = Solution()

root1 = TreeNode(1)
root1.left = TreeNode(2)
root1.right = TreeNode(3)
root1.left.left = TreeNode(4)
root1.left.right = TreeNode(-99)
root1.right.left = TreeNode(-99)
root1.right.right = TreeNode(7)
root1.left.left.left = TreeNode(8)
root1.left.left.right = TreeNode(9)
root1.left.right.left = TreeNode(-99)
root1.left.right.right = TreeNode(-99)
root1.right.left.left = TreeNode(12)
root1.right.left.right = TreeNode(13)
root1.right.right.left = TreeNode(-99)
root1.right.right.right = TreeNode(14)
print(s.sufficientSubset(root1, 1))

root2 = TreeNode(5)
root2.left = TreeNode(4)
root2.right = TreeNode(8)
root2.left.left = TreeNode(11)
root2.right.left = TreeNode(17)
root2.right.right = TreeNode(4)
root2.left.left.left = TreeNode(7)
root2.left.left.right = TreeNode(1)
root2.right.right.left = TreeNode(5)
root2.right.right.right = TreeNode(3)
print(s.sufficientSubset(root2, 22))

root3 = TreeNode(1)
root3.left = TreeNode(2)
root3.right = TreeNode(-3)
root3.left.left = TreeNode(-5)
root3.right.left = TreeNode(4)
print(s.sufficientSubset(root3, -1))
