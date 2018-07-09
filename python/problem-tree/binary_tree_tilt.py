#   https://leetcode.com/problems/binary-tree-tilt
#   27.30%

#   https://leetcode.com/problems/binary-tree-tilt/solution


from TreeNode import TreeNode


class Solution:
    def findTilt(self, root):
        if root is None:
            return 0
        res = 0
        queue, parentDict, maxLevel = [(root, None, 0)], {}, 0
        while queue:
            cur, parent, level = queue[0]
            del queue[0]
            parentDict[cur] = (parent, level, 0, 0)
            maxLevel = max(level, maxLevel)
            if cur.left:
                queue.append((cur.left, cur, level + 1))
            if cur.right:
                queue.append((cur.right, cur, level + 1))
        for node, (_, level, _, _) in sorted(parentDict.items(), key=lambda t: t[1][1], reverse=True):
            parent, _, lSum, rSum = parentDict[node]
            if parent is None:
                continue
            pParent, pLevel, pLSum, pRSum = parentDict[parent]
            if 0 == pLSum:
                parentDict[parent] = (pParent, pLevel, node.val + lSum + rSum, pRSum)
            else:
                parentDict[parent] = (pParent, pLevel, pLSum, node.val + lSum + rSum)
        tilt = 0
        for _, (_, level, lSum, rSum) in parentDict.items():
            if maxLevel == level:
                continue
            tilt += abs(lSum - rSum)
        return tilt


s = Solution()

'''
    1
   / \
  2   3
  2:1, 3:1
'''
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
print(s.findTilt(root)) #   1

'''
    1
   / \
  2   3
 /   /
4   5
1:(0, None), 2:(1, 1), 3:(1, 1), 4:(2, 2), 5:(2, 3)
4: (2, 2), 5: (2, 3), 2: (1, 1), 3: (1, 1), 1: (0, None)
4: (2, 2, 0, 0), 5: (2, 3, 0, 0)
2: (1, 1, 4, 0), 3: (1, 1, 5, 0)
1: (1, 1, 6, 8)
'''
root = TreeNode(1)
root.left = TreeNode(2)
root.left.left = TreeNode(4)
root.right = TreeNode(3)
root.right.left = TreeNode(5)
print(s.findTilt(root)) #   11

'''
    1
   /
  2
 / \
3   4
'''
root = TreeNode(1)
root.left = TreeNode(2)
root.left.left = TreeNode(3)
root.left.right = TreeNode(4)
print(s.findTilt(root)) #   10
