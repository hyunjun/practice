#   https://leetcode.com/problems/find-bottom-left-tree-value


from TreeNode import TreeNode

class Solution:
    #   runtime; 48ms, 100.00%
    #   memory; 15MB, 1.83%
    def findBottomLeftValue(self, root):
        if root is None:
            return None
        prevLv, q, ret = -1, [(0, root)], None
        while q:
            lv, node = q.pop(0)
            if prevLv != lv:
                ret = node.val
            prevLv = lv
            if node.left:
                q.append((lv + 1, node.left))
            if node.right:
                q.append((lv + 1, node.right))
        return ret


s = Solution()
root1 = TreeNode(2)
root1.left = TreeNode(1)
root1.right = TreeNode(3)
root2 = TreeNode(1)
root2.left = TreeNode(2)
root2.right = TreeNode(3)
root2.left.left = TreeNode(4)
root2.right.left = TreeNode(5)
root2.right.right = TreeNode(6)
root2.right.left.left = TreeNode(7)
data = [(root1, 1),
        (root2, 7),
        ]
for root, expected in data:
    real = s.findBottomLeftValue(root)
    print('{}, expected {}, real {}, result {}'.format(root, expected, real, expected == real))
