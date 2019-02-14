#   https://leetcode.com/problems/all-possible-full-binary-trees

#   https://leetcode.com/problems/all-possible-full-binary-trees/solution


from TreeNode import TreeNode
from collections import defaultdict

class Solution:
    #   runtime; 156ms, 95.02%
    #   memory; 15.8MB, 100.00%
    def allPossibleFBT(self, N):
        if N <= 0 or 0 == N % 2:
            return []

        treeDict = defaultdict(list)
        treeDict[1] = [TreeNode(0)]
        tree3 = TreeNode(0)
        tree3.left = TreeNode(0)
        tree3.right = TreeNode(0)
        treeDict[3] = [tree3]

        def trees(n):
            if n in treeDict:
                return treeDict[n]
            for lNum in range(1, n - 1):
                for l in trees(lNum):
                    for r in trees(n - 1 - lNum):
                        tree = TreeNode(0)
                        tree.left, tree.right = l, r
                        treeDict[n].append(tree)
            return treeDict[n]

        return trees(N)


s = Solution()
for root in s.allPossibleFBT(7):
    print(root)
