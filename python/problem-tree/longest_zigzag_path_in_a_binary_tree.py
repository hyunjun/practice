#   https://leetcode.com/problems/longest-zigzag-path-in-a-binary-tree


from TreeNode import TreeNode


class Solution:
    #   runtime; 684ms, 14.48%
    #   memory; 60.7MB, 100.00%
    def longestZigZag(self, root: TreeNode) -> int:
        if root is None:
            return 0

        self.maxLen = 0
        def zigzag(acc, node):
            self.maxLen = max(self.maxLen, len(acc))
            if (0 == len(acc) or acc[-1] == 0):
                if node.left:
                    zigzag([0], node.left)
                if node.right:
                    acc.append(1)
                    zigzag(acc, node.right)
                    acc.pop()
            if (0 == len(acc) or acc[-1] == 1):
                if node.left:
                    acc.append(0)
                    zigzag(acc, node.left)
                    acc.pop()
                if node.right:
                    zigzag([1], node.right)

        zigzag([], root)

        return self.maxLen


s = Solution()
root1 = TreeNode(1)
root1.right = TreeNode(1)
root1.right.left = TreeNode(1)
root1.right.right = TreeNode(1)
root1.right.right.left = TreeNode(1)
root1.right.right.right = TreeNode(1)
root1.right.right.left.right = TreeNode(1)
root1.right.right.left.right.right = TreeNode(1)
root2 = TreeNode(1)
root2.left = TreeNode(1)
root2.right = TreeNode(1)
root2.left.right = TreeNode(1)
root2.left.right.left = TreeNode(1)
root2.left.right.right = TreeNode(1)
root2.left.right.left.right = TreeNode(1)
root3 = TreeNode(1)
data = [(root1, 3),
        (root2, 4),
        (root3, 0),
        ]
for root, expected in data:
    real = s.longestZigZag(root)
    print(f'{root} expected {expected} real {real} result {expected == real}')
