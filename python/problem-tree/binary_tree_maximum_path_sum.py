#   https://leetcode.com/problems/binary-tree-maximum-path-sum


from TreeNode import TreeNode

class Solution:
    #   runtime; 88ms, 99.51%
    #   memory; 21.3MB, 100.00%
    def maxPathSum0(self, root):
        if root is None:
            return 0

        self.res = root.val

        def nodeSum(parentVal, node):
            if node is None:
                return 0
            lSum, rSum = None, None
            if node.left:
                lSum = nodeSum(node.val, node.left)
            if node.right:
                rSum = nodeSum(node.val, node.right)
            if lSum is None and rSum is None:
                self.res = max(self.res, node.val)
                return node.val
            if lSum is None:
                self.res = max(self.res, node.val, node.val + rSum, rSum)
                return max(node.val, node.val + rSum)
            if rSum is None:
                self.res = max(self.res, node.val, node.val + lSum, lSum)
                return max(node.val, node.val + lSum)
            self.res = max(self.res, node.val, node.val + lSum + rSum, node.val + lSum, lSum, node.val + rSum, rSum)
            return max(node.val, node.val + lSum, node.val + rSum)

        nodeSum(0, root)
        return self.res

    #   https://leetcode.com/submissions/detail/331729239/?from=/explore/challenge/card/30-day-leetcoding-challenge/532/week-5/3314
    #   runtime; 80ms, 97.00%
    #   memory; 21.5MB
    def maxPathSum(self, root):
        if root is None:
            return 0

        self.maxSum = float('-inf')
        def getMaxPath(node):
            if node is None:
                return 0
            lRes, rRes = getMaxPath(node.left), getMaxPath(node.right)
            if 0 < lRes and 0 < rRes:
                self.maxSum = max(self.maxSum, lRes + node.val + rRes)
            elif 0 < lRes:
                self.maxSum = max(self.maxSum, lRes + node.val)
            elif 0 < rRes:
                self.maxSum = max(self.maxSum, node.val + rRes)
            else:
                self.maxSum = max(self.maxSum, node.val)
            if lRes > rRes and lRes > 0:
                return node.val + lRes
            if lRes < rRes and rRes > 0:
                return node.val + rRes
            return node.val

        getMaxPath(root)
        return self.maxSum


s = Solution()
root1 = TreeNode(1)
root1.left = TreeNode(2)
root1.right = TreeNode(3)
root2 = TreeNode(-10)
root2.left = TreeNode(9)
root2.right = TreeNode(20)
root2.right.left = TreeNode(15)
root2.right.right = TreeNode(7)
root3 = TreeNode(2)
root3.left = TreeNode(-1)
root4 = TreeNode(1)
root4.left = TreeNode(-2)
root4.right = TreeNode(-3)
root4.left.left = TreeNode(1)
root4.left.right = TreeNode(3)
root4.right.left = TreeNode(-2)
root4.left.left.left = TreeNode(-1)
root5 = TreeNode(5)
root5.left = TreeNode(4)
root5.right = TreeNode(8)
root5.left.left = TreeNode(11)
root5.right.left = TreeNode(13)
root5.right.right = TreeNode(4)
root5.left.left.left = TreeNode(7)
root5.left.left.right = TreeNode(2)
root5.right.right.right = TreeNode(1)
root6 = TreeNode(-1)
root6.left = TreeNode(5)
root6.left.left = TreeNode(4)
root6.left.left.right = TreeNode(2)
root6.left.left.right.left = TreeNode(-4)
root7 = TreeNode(5)
root7.left = TreeNode(-5)
root7.right = TreeNode(-9)
root7.left.left = TreeNode(6)
root7.left.right = TreeNode(3)
root7.right.left = TreeNode(2)
root7.left.left.right = TreeNode(5)
root7.left.right.left = TreeNode(4)
root7.left.right.left.right = TreeNode(1)
data = [(root1, 6),
        (root2, 42),
        (TreeNode(-3), -3),
        (root3, 2),
        (root4, 3),
        (root5, 48),
        (root6, 11),
        (root7, 14),
        ]
for root, expected in data:
    real = s.maxPathSum(root)
    print('{}, expected {}, real {}, result {}'.format(root, expected, real, expected == real))
