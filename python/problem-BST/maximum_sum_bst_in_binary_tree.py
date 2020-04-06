#   https://leetcode.com/problems/maximum-sum-bst-in-binary-tree


from TreeNode import TreeNode


class Solution:
    #   runtime; 768ms, 6.70%
    #   memory; 67.7MB, 100.00%
    def maxSumBST(self, root: TreeNode) -> int:
        if root is None:
            return 0

        self.maxSum = 0

        def isBST(node, _min, _max):
            if node is None:
                return [True, 0]
            lRes, rRes = isBST(node.left, _min, node.val), isBST(node.right, node.val, _max)
            if node.left is not None and node.left.val >= node.val:
                lRes[0] = False
            if node.right is not None and node.val >= node.right.val:
                rRes[0] = False
            if lRes[0] and rRes[0]:
                curSum = lRes[1] + node.val + rRes[1]
                self.maxSum = max(self.maxSum, curSum)
                return [True, curSum]
            return [False, 0]

        isBST(root, float('-inf'), float('inf'))

        return self.maxSum


s = Solution()
root1 = TreeNode(1)
root1.left = TreeNode(4)
root1.left.left = TreeNode(2)
root1.left.right = TreeNode(4)
root1.right = TreeNode(3)
root1.right.left = TreeNode(2)
root1.right.right = TreeNode(5)
root1.right.right.left = TreeNode(4)
root1.right.right.right = TreeNode(6)
root2 = TreeNode(4)
root2.left = TreeNode(3)
root2.left.left = TreeNode(1)
root2.left.right = TreeNode(2)
root3 = TreeNode(-4)
root3.left = TreeNode(-2)
root3.right = TreeNode(-5)
root4 = TreeNode(2)
root4.left = TreeNode(1)
root4.right = TreeNode(3)
root5 = TreeNode(5)
root5.left = TreeNode(4)
root5.right = TreeNode(8)
root5.left.left = TreeNode(3)
root5.right.left = TreeNode(6)
root5.right.right = TreeNode(3)
data = [(root1, 20),
        (root2, 2),
        (root3, 0),
        (root4, 6),
        (root5, 7),
        ]
for root, expected in data:
    real = s.maxSumBST(root)
    print(f'{root} expected {expected} real {real} result {expected == real}')
