#   https://leetcode.com/problems/smallest-subtree-with-all-the-deepest-nodes
#   https://leetcode.com/problems/lowest-common-ancestor-of-deepest-leaves


from collections import defaultdict
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

    #   https://leetcode.com/explore/challenge/card/december-leetcoding-challenge/570/week-2-december-8th-december-14th/3563
    #   runtime; 36ms, 56.10%
    #   memory; 14.7MB
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        if root is None:
            return root
        q, depthDict, pDict = [(root, 0)], defaultdict(list), {}
        while q:
            n, d = q.pop(0)
            depthDict[d].append(n)
            if n.left:
                pDict[id(n.left)] = n
                q.append((n.left, d + 1))
            if n.right:
                pDict[id(n.right)] = n
                q.append((n.right, d + 1))
        maxDepth = max(depthDict.keys())
        deepestNodes = depthDict[maxDepth]
        if 1 == len(deepestNodes):
            return deepestNodes[0]
        #print([n.val for n in deepestNodes])
        allPDict = {}
        for n in deepestNodes:
            p, depth = n, maxDepth - 1
            while id(p) in pDict:
                p = pDict[id(p)]
                if id(p) not in allPDict:
                    allPDict[id(p)] = [p, depth, 0]
                allPDict[id(p)][2] += 1
                depth -= 1
        #print(allPDict)
        return sorted([(node, depth) for nodeId, (node, depth, cnt) in allPDict.items() if cnt == len(deepestNodes)], key=lambda t: -t[1])[0][0]


s = Solution()
'''
    1
   / \
  2   3
'''
root1 = TreeNode(1)
root1.left = TreeNode(2)
root1.right = TreeNode(3)
'''
    1
   / \
  2   3
 /
4
'''
root2 = TreeNode(1)
root2.left = TreeNode(2)
root2.right = TreeNode(3)
root2.left.left = TreeNode(4)
'''
    1
   / \
  2   3
 / \
4  5
'''
root3 = TreeNode(1)
root3.left = TreeNode(2)
root3.right = TreeNode(3)
root3.left.left = TreeNode(4)
root3.left.right = TreeNode(5)
'''
    1
   / \
  3   1
 /   /
4    2
 \    \
  6    5
'''
root4 = TreeNode(1)
root4.left = TreeNode(3)
root4.left.left = TreeNode(4)
root4.left.left.right = TreeNode(6)
root4.right = TreeNode(1)
root4.right.left = TreeNode(2)
root4.right.left.right = TreeNode(5)
for r in [root1, root2, root3, root4]:
    print(r)
    #print(s.lcaDeepestLeaves(r))
    print(s.subtreeWithAllDeepest(r))
