#   https://leetcode.com/problems/delete-nodes-and-return-forest


from TreeNode import TreeNode
from typing import List


class Solution:
    #   runtime; 68ms, 100.00%
    #   memory; 13.6MB, 100.00%
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        if root is None:
            return []
        if to_delete is None or 0 == len(to_delete):
            return root
        pDict, cDict, q = {}, {}, [(None, root)]
        while q:
            p, n = q.pop(0)
            pDict[n.val] = p
            cDict[n.val] = (n.left, n.right)
            if n.left:
                q.append((n, n.left))
            if n.right:
                q.append((n, n.right))
        res = []
        if root.val not in to_delete:
            res.append(root)
        for d in to_delete:
            p = pDict[d]
            if p:
                if p.left and p.left.val == d:
                    p.left = None
                elif p.right and p.right.val == d:
                    p.right = None
            l, r = cDict[d]
            if l and l.val not in to_delete:
                res.append(l)
            if r and r.val not in to_delete:
                res.append(r)
        return res


s = Solution()
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)
for n in s.delNodes(root, [3, 5]):
    print(n)
