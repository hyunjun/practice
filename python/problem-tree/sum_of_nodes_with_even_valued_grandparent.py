#   https://leetcode.com/problems/sum-of-nodes-with-even-valued-grandparent


from TreeNode import TreeNode


class Solution:
    #   runtime; 104ms, 63.27%
    #   memory; 17.4MB, 100.00%
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        if root is None:
            return 0

        self.sum = 0
        def traverse(n, isPPEven, isPEven):
            if n is None:
                return
            if isPPEven:
                self.sum += n.val
            isEven = True if n.val % 2 == 0 else False
            traverse(n.left, isPEven, isEven)
            traverse(n.right, isPEven, isEven)

        traverse(root, False, False)
        return self.sum


s = Solution()
root1 = TreeNode(6)
root1.left = TreeNode(7)
root1.left.left = TreeNode(2)
root1.left.left.left = TreeNode(9)
root1.left.right = TreeNode(7)
root1.left.right.left = TreeNode(1)
root1.left.right.right = TreeNode(4)
root1.right = TreeNode(8)
root1.right.left = TreeNode(1)
root1.right.right = TreeNode(3)
root1.right.right.right = TreeNode(5)
data = [(root1, 18),
        ]
for root, expected in data:
    real = s.sumEvenGrandparent(root)
    print(f'{root} expected {expected} real {real} result {expected == real}')
