#   https://leetcode.com/problems/find-largest-value-in-each-tree-row


from TreeNode import TreeNode
from collections import defaultdict
import sys

class Solution:
    #   runtime; 56ms, 87.71%
    #   memory; 15.1MB, 0.63%
    def largestValues(self, root):
        if root is None:
            return []
        d, q = defaultdict(lambda: -sys.maxsize), [(0, root)]
        while q:
            lv, node = q.pop(0)
            d[lv] = max(d[lv], node.val)
            if node.left:
                q.append((lv + 1, node.left))
            if node.right:
                q.append((lv + 1, node.right))
        return [val for _, val in sorted(d.items(), key=lambda t: t[0])]


s = Solution()
root = TreeNode(1)
root.left = TreeNode(3)
root.right = TreeNode(2)
root.left.left = TreeNode(5)
root.left.right = TreeNode(3)
root.right.right = TreeNode(9)
data = [(root, [1, 3, 9]),
        ]
for root, expected in data:
    real = s.largestValues(root)
    print('{}, expected {}, real {}, result {}'.format(root, expected, real, expected == real))
