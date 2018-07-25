#   https://leetcode.com/problems/average-of-levels-in-binary-tree

#   https://leetcode.com/problems/average-of-levels-in-binary-tree/solution


from TreeNode import TreeNode


class Solution:
    #   49.07%
    def averageOfLevels(self, root):
        if root is None:
            return []

        queue, res = [(root, 0)], []
        preLevel, vals = 0, []
        while queue:
            cur, level = queue.pop(0)
            if preLevel != level:
                res.append(sum(vals) / len(vals))
                preLevel = level
                vals = []
            vals.append(cur.val)
            if cur.left:
                queue.append((cur.left, level + 1))
            if cur.right:
                queue.append((cur.right, level + 1))
        res.append(sum(vals) / len(vals))
        return res


s = Solution()
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
print(s.averageOfLevels(root))
