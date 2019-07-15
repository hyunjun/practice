#   https://leetcode.com/problems/lowest-common-ancestor-of-deepest-leaves


from TreeNode import TreeNode


class Solution:
    #   runtime; 56ms, 69.66%
    #   memory; 13.4MB, 100.00%
    def lcaDeepestLeaves(self, root: TreeNode) -> TreeNode:
        if root is None:
            return None
        pDict, q, maxDepth, deepestLeaves = {}, [(0, None, root)], 0, []
        while q:
            d, p, n = q.pop(0)
            if maxDepth < d:
                maxDepth, deepestLeaves = d, [n]
            elif maxDepth == d:
                deepestLeaves.append(n)
            pDict[n] = p
            if n.left:
                q.append((d + 1, n, n.left))
            if n.right:
                q.append((d + 1, n, n.right))
        if 1 == len(deepestLeaves):
            return deepestLeaves[0]
        parents = [[] for _ in range(len(deepestLeaves))]
        for i, deepestLeaf in enumerate(deepestLeaves):
            p = pDict[deepestLeaf]
            while p in pDict:
                parents[i].append(p)
                p = pDict[p]
        for i, p in enumerate(parents[0]):
            if all(parents[r][i] == p for r in range(len(parents))):
                return p
        return None


s = Solution()
root1 = TreeNode(1)
root1.left = TreeNode(2)
root1.right = TreeNode(3)
root2 = TreeNode(1)
root2.left = TreeNode(2)
root2.right = TreeNode(3)
root2.left.left = TreeNode(4)
root3 = TreeNode(1)
root3.left = TreeNode(2)
root3.right = TreeNode(3)
root3.left.left = TreeNode(4)
root3.left.right = TreeNode(5)
for r in [root1, root2, root3]:
    print(r)
    print(s.lcaDeepestLeaves(r))
