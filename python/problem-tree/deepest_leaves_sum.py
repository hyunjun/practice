#   https://leetcode.com/problems/deepest-leaves-sum


from TreeNode import TreeNode
from collections import defaultdict


class Solution:
    #   runtime; 92ms, 75.37%
    #   memory; 16.2MB, 100.00%
    def deepestLeavesSum0(self, root: TreeNode) -> int:
        if root is None:
            return 0
        maxDepth, leavesSum, q = 0, 0, [(0, root)]
        while q:
            depth, n = q.pop(0)
            if n.left is None and n.right is None:
                if depth == maxDepth:
                    leavesSum += n.val
                elif maxDepth < depth:
                    maxDepth, leavesSum = depth, n.val
            if n.left:
                q.append((depth + 1, n.left))
            if n.right:
                q.append((depth + 1, n.right))
        return leavesSum

    #   runtime; 88ms, 88.10%
    #   memory; 16.1MB, 100.00%
    def deepestLeavesSum1(self, root: TreeNode) -> int:
        if root is None:
            return 0
        self.res, self.maxDepth = 0, 0
        def leaves(node, depth):
            if node.left is None and node.right is None:
                if self.maxDepth == depth:
                    self.res += node.val
                elif self.maxDepth < depth:
                    self.maxDepth, self.res = depth, node.val
            else:
                if node.left:
                    leaves(node.left, depth + 1)
                if node.right:
                    leaves(node.right, depth + 1)
        leaves(root, 0)
        return self.res

    #   runtime; 100ms, 48.64%
    #   memory; 16.1MB, 100.00%
    def deepestLeavesSum2(self, root: TreeNode) -> int:
        if root is None:
            return 0
        self.res, self.maxDepth = 0, 0
        def inorder(node, depth):
            if node.left:
                inorder(node.left, depth + 1)
            if node.left is None and node.right is None:
                if self.maxDepth == depth:
                    self.res += node.val
                elif self.maxDepth < depth:
                    self.maxDepth, self.res = depth, node.val
            if node.right:
                inorder(node.right, depth + 1)
        inorder(root, 0)
        return self.res

    #   runtime; 92ms, 75.37%
    #   memory; 16.2MB, 100.00%
    def deepestLeavesSum3(self, root: TreeNode) -> int:
        if root is None:
            return 0
        d, q = defaultdict(int), [(0, root)]
        while q:
            depth, n = q.pop(0)
            if n.left is None and n.right is None:
                d[depth] += n.val
            if n.left:
                q.append((depth + 1, n.left))
            if n.right:
                q.append((depth + 1, n.right))
        return sorted(d.items(), key=lambda t: t[0])[-1][1]

    #   https://leetcode.com/explore/challenge/card/april-leetcoding-challenge-2021/594/week-2-april-8th-april-14th/3704
    #   runtime: 104ms, 24.26%
    #   memory usage: 17.9MB, 34.98%
    def deepestLeavesSum4(self, root: TreeNode) -> int:
        if root is None:
            return 0
        maxDepth, curSum, q = 0, 0, [(root, 1)]
        while q:
            n, d = q.pop(0)
            if n.left is None and n.right is None:
                if d > maxDepth:
                    maxDepth, curSum = d, n.val
                elif d == maxDepth:
                    curSum += n.val
            if n.left:
                q.append((n.left, d + 1))
            if n.right:
                q.append((n.right, d + 1))
        return curSum

    #   runtime: 100ms, 33.35%
    #   memory usage: 17.7MB, 88.56%
    def deepestLeavesSum(self, root: TreeNode) -> int:
        self.maxDepth, self.curSum = 0, 0

        def traverseAndSum(node, depth):
            if node is None:
                return
            if node.left is None and node.right is None:
                if depth > self.maxDepth:
                    self.maxDepth, self.curSum = depth, node.val
                elif depth == self.maxDepth:
                    self.curSum += node.val
            traverseAndSum(node.left, depth + 1)
            traverseAndSum(node.right, depth + 1)

        traverseAndSum(root, 1)

        return self.curSum


s = Solution()
root1 = TreeNode(1)
root1.left = TreeNode(2)
root1.right = TreeNode(3)
root1.left.left = TreeNode(4)
root1.left.right = TreeNode(5)
root1.right.right = TreeNode(6)
root1.left.left.left = TreeNode(7)
root1.right.right.right = TreeNode(8)
data = [(root1, 15),
        ]
for root, expected in data:
    real = s.deepestLeavesSum(root)
    print(f'{root} expected {expected} real {real} result {expected == real}')
