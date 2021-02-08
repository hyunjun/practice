#   https://leetcode.com/problems/binary-tree-level-order-traversal-ii


from TreeNode import TreeNode
from collections import defaultdict
from typing import List


class Solution(object):
    #   100.00%
    def levelOrderBottom0(self, root):
        if root is None:
            return []
        q, result = [(root, 1)], []
        while 0 < len(q):
            cur, level = q[0]
            if len(result) < level:
                result.append([cur.val])
            else:
                result[level - 1].append(cur.val)
            if cur.left is not None:
                q.append((cur.left, level + 1))
            if cur.right is not None:
                q.append((cur.right, level + 1))
            del q[0]
        return result[::-1]

    #   https://leetcode.com/explore/featured/card/july-leetcoding-challenge/544/week-1-july-1st-july-7th/3378
    #   runtime; 48ms, 15.71%
    #   memory; 14MB, 75.41%
    def levelOrderBottom1(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []
        queue, d = [(root, 1)], defaultdict(list)
        while queue:
            node, depth = queue.pop(0)
            d[depth].append(node.val)
            if node.left:
                queue.append((node.left, depth + 1))
            if node.right:
                queue.append((node.right, depth + 1))
        return [v for _, v in sorted(d.items(), key=lambda t: -t[0])]

    #   runtime; 40ms, 32.63%
    #   memory; 14.2MB, 29.86%
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []
        queue, d = [(root, 1)], defaultdict(list)
        while queue:
            node, depth = queue.pop(0)
            d[depth].append(node.val)
            if node.left:
                queue.append((node.left, depth + 1))
            if node.right:
                queue.append((node.right, depth + 1))
        return [d[i] for i in range(depth, 0, -1)]


root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
root.right.right.right = TreeNode(9)
root.right.right.right.left = TreeNode(11)
s = Solution()
print(s.levelOrderBottom(root))
