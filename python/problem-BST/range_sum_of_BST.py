#   https://leetcode.com/problems/range-sum-of-bst

#   https://leetcode.com/problems/range-sum-of-bst/solution


from TreeNode import TreeNode


class Solution:
    #   540ms, 9.17%
    def rangeSumBST0(self, root, L, R):
        self._sum = 0
        def add(node):
            if node is None:
                return
            if L <= node.val <= R:
                self._sum += node.val
            add(node.left)
            add(node.right)
        add(root)
        return self._sum

    #   572ms, 5.37%
    def rangeSumBST1(self, root, L, R):
        if root is None:
            return 0
        q, _sum = [root], 0
        while q:
            n = q.pop(0)
            if L <= n.val <= R:
                _sum += n.val
            if n.left:
                q.append(n.left)
            if n.right:
                q.append(n.right)
        return _sum

    #   https://leetcode.com/explore/challenge/card/november-leetcoding-challenge/566/week-3-november-15th-november-21st/3532
    #   runtime; 208ms, 78.22%
    #   memory; 22MB, 62.06%
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        if root is None:
            return 0
        res, q = 0, [(root, float('-inf'), float('inf'))]
        while q:
            n, minVal, maxVal = q.pop(0)
            if maxVal < low or high < minVal:
                continue
            if low <= n.val <= high:
                res += n.val
            if n.left:
                q.append((n.left, minVal, n.val - 1))
            if n.right:
                q.append((n.right, n.val + 1, maxVal))
        return res


s = Solution()
root1 = TreeNode(10)
root1.left = TreeNode(5)
root1.left.left = TreeNode(3)
root1.left.right = TreeNode(7)
root1.right = TreeNode(15)
root1.right.right = TreeNode(18)
root2 = TreeNode(10)
root2.left = TreeNode(5)
root2.left.left = TreeNode(3)
root2.left.left.left = TreeNode(1)
root2.left.right = TreeNode(7)
root2.left.right.left = TreeNode(6)
root2.right = TreeNode(15)
root2.right.left = TreeNode(13)
root2.right.right = TreeNode(18)
data = [(root1, 7, 15, 32),
        (root2, 6, 10, 23),
        ]
for root, low, high, expect in data:
    real = s.rangeSumBST(root, low, high)
    print(f'{root} {low} {high} expect {expect} real {real} result {expect == real}')
