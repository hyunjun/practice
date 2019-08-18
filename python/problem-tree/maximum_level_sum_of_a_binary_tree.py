#   https://leetcode.com/problems/maximum-level-sum-of-a-binary-tree


from collections import defaultdict
from TreeNode import TreeNode


class Solution:
    #   runtime; 372ms, 100.00%
    #   memory; 18.6MB, 100.00%
    def maxLevelSum(self, root: TreeNode) -> int:
        if root is None:
            return 0
        d, q = defaultdict(int), [(1, root, 0)]
        while q:
            lv, node, curSum = q.pop(0)
            d[lv] += node.val
            if node.left:
                q.append((lv + 1, node.left, curSum))
            if node.right:
                q.append((lv + 1, node.right, curSum))
        maxLv, maxSum = 0, 0
        for i in range(1, max(d.keys()) + 1):
            if maxSum < d[i]:
                maxLv, maxSum = i, d[i]
        return maxLv


s = Solution()
root1 = TreeNode(1)
root1.left = TreeNode(7)
root1.right = TreeNode(0)
root1.left.left = TreeNode(7)
root1.left.right = TreeNode(-8)
root2 = TreeNode(989)
root2.right = TreeNode(10250)
root2.right.left = TreeNode(98693)
root2.right.right = TreeNode(-89388)
root2.right.right.right = TreeNode(-32127)
data = [(root1, 2),
        (root2, 2),
        ]
for root, expected in data:
    real = s.maxLevelSum(root)
    print(f'{root}, expected {expected}, real {real}, result {expected == real}')
