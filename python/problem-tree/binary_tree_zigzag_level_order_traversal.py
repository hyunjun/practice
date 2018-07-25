#   https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal


from TreeNode import TreeNode


class Solution:
    #   1.34%
    def zigzagLevelOrder(self, root):
        if root is None:
            return []
        queue, res = [(root, 0)], []
        preLevel, vals = 0, []
        while queue:
            cur, level = queue.pop(0)
            if preLevel != level:
                if 0 == preLevel % 2:
                    res.append(vals)
                else:
                    res.append(vals[::-1])
                preLevel, vals = level, []
            vals.append(cur.val)
            if cur.left:
                queue.append((cur.left, level + 1))
            if cur.right:
                queue.append((cur.right, level + 1))
        if 0 == preLevel % 2:
            res.append(vals)
        else:
            res.append(vals[::-1])
        return res


s = Solution()
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
print(s.zigzagLevelOrder(root))
