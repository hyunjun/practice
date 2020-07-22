#   https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal


from TreeNode import TreeNode
from collections import defaultdict
from typing import List


class Solution:
    #   1.34%
    def zigzagLevelOrder0(self, root):
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

    #   https://leetcode.com/explore/featured/card/july-leetcoding-challenge/547/week-4-july-22nd-july-28th/3398
    #   runtime; 48ms, 22.10%
    #   memory; 14.1MB, 29.05%
    def zigzagLevelOrder1(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []
        q, d = [(root, 0)], defaultdict(list)
        while q:
            n, depth = q.pop(0)
            d[depth].append(n.val)
            if n.left:
                q.append((n.left, depth + 1))
            if n.right:
                q.append((n.right, depth + 1))
        res = []
        for i in range(depth + 1):
            if i % 2 == 0:
                res.append(d[i])
            else:
                res.append(d[i][::-1])
        return res

    #   runtime; 36ms, 56.40%
    #   memory; 14.1MB, 25.90%
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []
        q, vals, prevDepth, res = [(root, 0)], [], 0, []
        while q:
            n, depth = q.pop(0)
            if prevDepth != depth:
                if prevDepth % 2 == 0:
                    res.append(vals)
                else:
                    res.append(vals[::-1])
                vals = []
                prevDepth = depth
            vals.append(n.val)
            if n.left:
                q.append((n.left, depth + 1))
            if n.right:
                q.append((n.right, depth + 1))
        if prevDepth % 2 == 0:
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
