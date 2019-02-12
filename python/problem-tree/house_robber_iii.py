#   https://leetcode.com/problems/house-robber-iii

#   https://leetcode.com/problems/house-robber-iii/discuss/79330/Step-by-step-tackling-of-the-problem


from TreeNode import TreeNode

class Solution:
    #   Wrong Answer
    def rob0(self, root):
        if root is None:
            return 0
        lvSums, q = {}, [(0, root)]
        while q:
            lv, node = q.pop(0)
            if lv in lvSums:
                lvSums[lv] += node.val
            else:
                lvSums[lv] = node.val
            if node.left:
                q.append((lv + 1, node.left))
            if node.right:
                q.append((lv + 1, node.right))
        curMax = 0
        for lv, curSum in sorted(lvSums.items(), key=lambda t: t[0]):
            if 2 < lv:
                lvSums[lv] += max(lvSums[lv - 3], lvSums[lv - 2])
            elif 1 < lv:
                lvSums[lv] += lvSums[lv - 2]
            curMax = max(curMax, lvSums[lv])
        return curMax

    #   Time Limit Exceeded
    def rob1(self, root):
        if root is None:
            return 0
        val = 0
        if root.left:
            val += self.rob1(root.left.left) + self.rob1(root.left.right)
        if root.right:
            val += self.rob1(root.right.left) + self.rob1(root.right.right)
        return max(val + root.val, self.rob1(root.left) + self.rob1(root.right))

    #   runtime; 104ms, 12.35%
    #   memory; 15.3MB, 0.80%
    def rob(self, root):
        memo = {}
        def _rob(node):
            if node in memo:
                return memo[node]
            if node is None:
                return 0
            val = 0
            if node.left:
                val += _rob(node.left.left) + _rob(node.left.right)
            if node.right:
                val += _rob(node.right.left) + _rob(node.right.right)
            val = max(val + node.val, _rob(node.left) + _rob(node.right))
            memo[node] = val
            return val

        return _rob(root)


s = Solution()
root1 = TreeNode(3)
root1.left = TreeNode(2)
root1.right = TreeNode(3)
root1.left.right = TreeNode(3)
root1.right.right = TreeNode(1)
root2 = TreeNode(3)
root2.left = TreeNode(4)
root2.right = TreeNode(5)
root2.left.left = TreeNode(1)
root2.left.right = TreeNode(3)
root2.right.right = TreeNode(1)
root3 = TreeNode(4)
root3.left = TreeNode(1)
root3.left.left = TreeNode(2)
root3.left.left.left = TreeNode(3)
root4 = TreeNode(2)
root4.left = TreeNode(1)
root4.right = TreeNode(3)
root4.left.right = TreeNode(4)
data = [(root1, 7),
        (root2, 9),
        (root3, 7),
        (root4, 7),
        ]
for root, expected in data:
    real = s.rob(root)
    print('{}, expected {}, real {}, result {}'.format(root, expected, real, expected == real))
