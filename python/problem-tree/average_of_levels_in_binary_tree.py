#   https://leetcode.com/problems/average-of-levels-in-binary-tree

#   https://leetcode.com/problems/average-of-levels-in-binary-tree/solution


from TreeNode import TreeNode
from typing import List


class Solution:
    #   49.07%
    def averageOfLevels0(self, root):
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

    #   https://leetcode.com/explore/challenge/card/march-leetcoding-challenge-2021/588/week-1-march-1st-march-7th/3661
    #   runtime: 52ms, 55.44%
    #   memory: 16.6MB, 36.25%
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        q, levels, levelCnt = [(root, 0)], [], 0
        while q:
            n, d = q.pop(0)
            if len(levels) == d:
                if 0 < len(levels):
                    levels[-1] /= levelCnt
                    levelCnt = 0
                levels.append(n.val)
            else:
                levels[-1] += n.val
            levelCnt += 1
            if n.left:
                q.append((n.left, d + 1))
            if n.right:
                q.append((n.right, d + 1))
        levels[-1] /= levelCnt
        return levels


s = Solution()
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
data = [(root, [3, 14.5, 11]),
        ]
for root, expect in data:
    real = s.averageOfLevels(root)
    print(f'{root} expect {expect} real {real} result {expect == real}')
