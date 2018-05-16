import math


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __str__(self):
        lVal, rVal = 'x', 'x'
        if self.left is None and self.right is None:
            lVal, rVal = '', ''
        if self.left:
            lVal = self.left
        if self.right:
            rVal = self.right
        return '({} {} {})'.format(lVal, self.val, rVal)


class Solution:
    def serialize(self, root):
        if root is None:
            return []
        queue = [(root, 0)]
        while queue:
            cur, level = queue[0]
            del queue[0]
            if cur.left:
                queue.append((cur.left, level + 1))
            if cur.right:
                queue.append((cur.right, level + 1))
        totalCnt = 0
        for i in range(level + 1):
            totalCnt += math.pow(2, i)
        treeList = [None] * (int)(totalCnt)
        queue = [(root, 0)]
        while queue:
            cur, idx = queue[0]
            del queue[0]
            if cur:
                treeList[idx] = cur.val
                if cur.left:
                    queue.append((cur.left, 2 * idx + 1))
                if cur.right:
                    queue.append((cur.right, 2 * idx + 2))
        return treeList

    def deserialize(self, treeList):
        if treeList is None or 0 == len(treeList):
            return None
        nodes = [None] * len(treeList)
        root = TreeNode(treeList[0])
        nodes[0] = root
        for i in range(1, len(treeList)):
            if treeList[i] is None:
                continue
            cur = TreeNode(treeList[i])
            nodes[i] = cur
            if i % 2 == 1:
                parentIdx = (i - 1) // 2
                parentNode = nodes[parentIdx]
                parentNode.left = cur
            else:
                parentIdx = (i - 2) // 2
                parentNode = nodes[parentIdx]
                parentNode.right = cur
        return root



'''
        _______2______
       /              \
    __3__           ___x__
   /     \         /      \
  x       1        x       x
'''
s = Solution()
root = TreeNode(2)
root.left = TreeNode(3)
root.left.right = TreeNode(1)
print(root)
treeList = s.serialize(root)
print(treeList)
root = s.deserialize(treeList)
print(root)
