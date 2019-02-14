#   https://leetcode.com/problems/check-completeness-of-a-binary-tree

#   https://leetcode.com/problems/check-completeness-of-a-binary-tree/solution


from TreeNode import TreeNode

class Solution:
    #   runtime; 40ms, 98.51%
    #   memory; 12.7MB, 100.00%
    def isCompleteTree(self, root):
        if root is None:
            return True
        q, res = [root], []
        while q:
            node = q.pop(0)
            if node:
                res.append(node.val)
                q.append(node.left)
                q.append(node.right)
            else:
                res.append(None)
        while res[-1] is None:
            res.pop()
        return None not in res


s = Solution()
root1 = TreeNode(1)
root1.left = TreeNode(2)
root1.right = TreeNode(3)
root1.left.left = TreeNode(4)
root1.left.right = TreeNode(5)
root1.right.left = TreeNode(6)
root2 = TreeNode(1)
root2.left = TreeNode(2)
root2.right = TreeNode(3)
root2.left.left = TreeNode(4)
root2.left.right = TreeNode(5)
root2.right.right = TreeNode(7)
root3 = TreeNode(1)
root3.left = TreeNode(2)
root3.right = TreeNode(3)
root3.left.left = TreeNode(4)
root3.right.left = TreeNode(6)
root3.right.right = TreeNode(7)
root4 = TreeNode(1)
root4.left = TreeNode(2)
root4.right = TreeNode(3)
root4.right.left = TreeNode(6)
root4.right.right = TreeNode(7)
data = [(root1, True),
        (root2, False),
        (root3, False),
        (root4, False),
        ]
for root, expected in data:
    real = s.isCompleteTree(root)
    print('{}, expected {}, real {}, result {}'.format(root, expected, real, expected == real))
