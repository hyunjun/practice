#   https://leetcode.com/problems/leaf-similar-trees

#   https://leetcode.com/problems/leaf-similar-trees/solution


from TreeNode import TreeNode


class Solution:
    #   17.45%
    def leafSimilar(self, root1, root2):
        if root1 is None and root2 is None:
            return True

        def leaves(node):
            cur, stack, res = node, [], []
            while cur or stack:
                if cur:
                    stack.append(cur)
                    cur = cur.left
                else:
                    cur = stack.pop()
                    if cur.left is None and cur.right is None:
                        res.append(cur.val)
                    cur = cur.right
            return res

        return leaves(root1) == leaves(root2)


s = Solution()

root1 = TreeNode(3)
root1.left = TreeNode(5)
root1.left.left = TreeNode(6)
root1.left.right = TreeNode(2)
root1.left.right.left = TreeNode(7)
root1.left.right.right = TreeNode(4)
root1.right = TreeNode(1)
root1.right.left = TreeNode(9)
root1.right.right = TreeNode(8)
root2 = TreeNode(3)
root2.left = TreeNode(5)
root2.left.left = TreeNode(6)
root2.left.right = TreeNode(7)
root2.right = TreeNode(1)
root2.right.left = TreeNode(4)
root2.right.right = TreeNode(2)
root2.right.right.left = TreeNode(9)
root2.right.right.right = TreeNode(8)
print(s.leafSimilar(root1, root2))
