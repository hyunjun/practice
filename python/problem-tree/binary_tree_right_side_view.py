#   https://leetcode.com/problems/binary-tree-right-side-view

#   https://leetcode.com/problems/binary-tree-right-side-view/solution


from TreeNode import TreeNode
from collections import defaultdict
from typing import List


class Solution:
    #   100.00%
    def rightSideView0(self, root):
        if root is None:
            return []
        res, queue = [], [(root, 0)]
        while queue:
            cur, depth = queue.pop(0)
            if len(res) == depth:
                res.append(cur.val)
            else:
                res[depth] = cur.val
            if cur.left:
                queue.append((cur.left, depth + 1))
            if cur.right:
                queue.append((cur.right, depth + 1))
        return res

    #   https://leetcode.com/explore/challenge/card/february-leetcoding-challenge-2021/584/week-1-february-1st-february-7th/3630
    #   runtime; 32ms, 71.27%
    #   memory; 14.3MB, 55.13%
    def rightSideView(self, root: TreeNode) -> List[int]:
        if root is None:
            return []
        q, d, maxDepth = [(0, root)], defaultdict(int), 0
        while q:
            depth, node = q.pop(0)
            maxDepth = max(maxDepth, depth)
            d[depth] = node.val
            if node.left:
                q.append((depth + 1, node.left))
            if node.right:
                q.append((depth + 1, node.right))
        return [d[i] for i in range(maxDepth + 1)]


s = Solution()

root = TreeNode(1)
root.left = TreeNode(2)
root.left.right = TreeNode(5)
root.right = TreeNode(3)
root.right.right = TreeNode(4)
print(s.rightSideView(root) == [1, 3, 4])

root = TreeNode(1)
root.left = TreeNode(2)
root.left.right = TreeNode(5)
root.right = TreeNode(3)
print(s.rightSideView(root) == [1, 3, 5])
