#   https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/532/week-5/3315


from TreeNode import TreeNode
from typing import List


class Solution:
    #   runtime; 116ms
    #   memory; 15.2MB
    def isValidSequence(self, root: TreeNode, arr: List[int]) -> bool:
        if root is None or arr is None or not (1 <= len(arr) <= 5000):
            return False

        def checkNodeVal(node, seq):
            if node is not None and 0 < len(seq) and node.val == seq[0]:
                if node.left is None and node.right is None and 1 == len(seq):
                    return True
                return checkNodeVal(node.left, seq[1:]) or checkNodeVal(node.right, seq[1:])
            return False

        return checkNodeVal(root, arr)


s = Solution()
root1 = TreeNode(0)
root1.left = TreeNode(1)
root1.left.left = TreeNode(0)
root1.left.left.right = TreeNode(1)
root1.left.right = TreeNode(1)
root1.left.right.left = TreeNode(0)
root1.left.right.right = TreeNode(0)
root1.right = TreeNode(0)
root1.right.left = TreeNode(0)
data = [(root1, [0, 1, 0, 1], True),
        (root1, [0, 0, 1], False),
        (root1, [0, 1, 1], False),
        ]
for root, arr, expected in data:
    real = s.isValidSequence(root, arr)
    print(f'{root} {arr} expected {expected} real {real} result {expected == real}')
