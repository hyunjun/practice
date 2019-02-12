#   https://leetcode.com/problems/most-frequent-subtree-sum


from TreeNode import TreeNode
from collections import defaultdict

class Solution:
    #   runtime; 52ms, 100.00%
    #   memory; 16.2MB, 0.71%
    def findFrequentTreeSum(self, root):
        if root is None:
            return []
        cDict = defaultdict(int)
        def _sum(node):
            if node is None:
                return 0
            lSum, rSum = 0, 0
            if node.left:
                lSum = _sum(node.left)
                cDict[lSum] += 1
            if node.right:
                rSum = _sum(node.right)
                cDict[rSum] += 1
            cSum = node.val + lSum + rSum
            cDict[cSum] += 1
            return cSum

        total = _sum(root)
        cDict[total] += 1
        maxCnt = max(cDict.values())
        return [s for s, cnt in cDict.items() if cnt == maxCnt]


s = Solution()
root1 = TreeNode(5)
root1.left = TreeNode(2)
root1.right = TreeNode(-3)
root2 = TreeNode(5)
root2.left = TreeNode(2)
root2.right = TreeNode(-5)
data = [(root1, [2, -3, 4]),
        (root2, [2]),
        ]
for root, expected in data:
    real = s.findFrequentTreeSum(root)
    print('{}, expected {}, real {}, result {}'.format(root, expected, real, sorted(expected) == sorted(real)))
