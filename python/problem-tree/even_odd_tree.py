#   https://leetcode.com/problems/even-odd-tree


from TreeNode import TreeNode
from collections import defaultdict


class Solution:
    #   runtime; 684ms, 20.00% -> 668ms, 20.00%
    #   memory; 56.2MB, 20.00% -> 56.1MB, 20.00%
    def isEvenOddTree(self, root: TreeNode) -> bool:
        q, d = [(root, 0)], defaultdict(list)
        while q:
            n, level = q.pop(0)
            #   다음과 같이 변경해서 약간의 성능 개선
            #if (level % 2 == 0 and n.val % 2 == 0) or (level % 2 == 1 and n.val % 2 == 1):
            if level % 2 == n.val % 2:
                return False
            d[level].append(n.val)
            if n.left:
                q.append((n.left, level + 1))
            if n.right:
                q.append((n.right, level + 1))
        level = 0
        while 0 < len(d[level]):
            if level % 2 == 0:
                for i, n in enumerate(d[level]):
                    if 0 == i:
                        continue
                    if d[level][i - 1] >= n:
                        return False
            else:
                for i, n in enumerate(d[level]):
                    if 0 == i:
                        continue
                    if d[level][i - 1] <= n:
                        return False
            level += 1
        return True

