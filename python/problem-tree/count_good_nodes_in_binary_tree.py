#   https://leetcode.com/problems/count-good-nodes-in-binary-tree


from TreeNode import TreeNode


class Solution:
    #   runtime; 532ms, 33.33%
    #   memory; 32.6MB, 100.00%
    def goodNodes(self, root: TreeNode) -> int:
        if root is None:
            return 0
        q, cnt = [(root.val, root)], 0
        while q:
            maxVal, n = q.pop(0)
            if maxVal <= n.val:
                cnt += 1
            maxVal = max(maxVal, n.val)
            if n.left:
                q.append((maxVal, n.left))
            if n.right:
                q.append((maxVal, n.right))
        return cnt


s = Solution()
root1 = TreeNode(3)
root1.left = TreeNode(1)
root1.right = TreeNode(4)
root1.left.left = TreeNode(3)
root1.right.left = TreeNode(1)
root1.right.right = TreeNode(5)
root2 = TreeNode(3)
root2.left = TreeNode(3)
root2.left.left = TreeNode(4)
root2.left.right = TreeNode(2)
data = [(root1, 4),
        (root2, 3),
        (TreeNode(1), 1),
        ]
for root, expected in data:
    real = s.goodNodes(root)
    print(f'{root} expected {expected} real {real} result {expected == real}')
