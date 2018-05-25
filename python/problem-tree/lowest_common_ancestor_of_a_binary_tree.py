#   https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree

#   https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/discuss/65225/4-lines-C++JavaPythonRuby
#   https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/discuss/65236/JavaPython-iterative-solution


class TreeNode:
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

    #   Runtime Error
    def lowestCommonAncestor0(self, root, p, q):
        if root is None or p is None or q is None:
            return None
        if root is p or root is q:
            return root
        if p is q:
            return p
        isPFound, isQFound = False, False
        queue, depth = [(root, 0)], -1
        while queue:
            cur, depth = queue[0]
            del queue[0]
            if cur is p:
                isPFound = True
            if cur is q:
                isQFound = True
            if isPFound and isQFound:
                break
            if cur.left:
                queue.append((cur.left, depth + 1))
            if cur.right:
                queue.append((cur.right, depth + 1))
        nodes = [None] * sum([2 ** i for i in range(depth + 1)])
        print(depth, len(nodes))
        isPFound, isQFound = False, False
        pIdx, qIdx = -1, -1
        queue = [(root, 0)]
        while queue:
            cur, idx = queue[0]
            del queue[0]
            nodes[idx] = cur
            if cur is p:
                isPFound, pIdx = True, idx
            if cur is q:
                isQFound, qIdx = True, idx
            if isPFound and isQFound:
                break
            if cur.left:
                queue.append((cur.left, 2 * idx + 1))
            if cur.right:
                queue.append((cur.right, 2 * idx + 2))
        print([node.val if node else 'x' for node in nodes])
        print(pIdx, qIdx)
        pParentsIndices, qParentsIndices = [], []
        while 0 <= pIdx:
            pParentsIndices.append(pIdx)
            if pIdx % 2 == 1:
                pIdx = (pIdx - 1) // 2
            else:
                pIdx = (pIdx - 2) // 2
        while 0 <= qIdx:
            qParentsIndices.append(qIdx)
            if qIdx % 2 == 1:
                qIdx = (qIdx - 1) // 2
            else:
                qIdx = (qIdx - 2) // 2
        return nodes[max(set(pParentsIndices).intersection(set(qParentsIndices)))]

    #   2.39%
    def lowestCommonAncestorByIdx(self, root, p, q):
        if root is None or p is None or q is None:
            return None
        if root is p or root is q:
            return root
        if p is q:
            return p
        isPFound, isQFound = False, False
        queue, pIdx, qIdx = [(root, 0)], -1, -1
        while queue:
            cur, idx = queue[0]
            del queue[0]
            if cur is p:
                isPFound, pIdx = True, idx
            if cur is q:
                isQFound, qIdx = True, idx
            if isPFound and isQFound:
                break
            if cur.left:
                queue.append((cur.left, 2 * idx + 1))
            if cur.right:
                queue.append((cur.right, 2 * idx + 2))
        print(pIdx, qIdx)
        pParentsIndices, qParentsIndices = [], []
        while 0 <= pIdx:
            pParentsIndices.append(pIdx)
            if pIdx % 2 == 1:
                pIdx = (pIdx - 1) // 2
            else:
                pIdx = (pIdx - 2) // 2
        while 0 <= qIdx:
            qParentsIndices.append(qIdx)
            if qIdx % 2 == 1:
                qIdx = (qIdx - 1) // 2
            else:
                qIdx = (qIdx - 2) // 2
        lcaIdx = max(set(pParentsIndices).intersection(set(qParentsIndices)))
        queue = [(root, 0)]
        while queue:
            cur, idx = queue[0]
            del queue[0]
            if idx == lcaIdx:
                return cur
            if cur.left:
                queue.append((cur.left, 2 * idx + 1))
            if cur.right:
                queue.append((cur.right, 2 * idx + 2))
        return None

    #   97.49%
    def lowestCommonAncestor(self, root, p, q):
        if root is None or p is None or q is None:
            return None
        if root is p or root is q:
            return root
        if p is q:
            return p
        queue, nodeParentDict = [(root, None)], {}
        while not (p in nodeParentDict and q in nodeParentDict):
            cur, parent = queue[0]
            del queue[0]
            nodeParentDict[cur] = parent
            if cur.left:
                queue.append((cur.left, cur))
            if cur.right:
                queue.append((cur.right, cur))
        parentSet = set()
        parentSet.add(p)
        while p:
            parent = nodeParentDict[p]
            parentSet.add(parent)
            p = parent
        while q:
            if q in parentSet:
                return q
            q = nodeParentDict[q]
        return None

'''
        _______3______
       /              \
    ___5__          ___1__
   /      \        /      \
   6      _2       0       8
         /  \
         7   4
'''
root = TreeNode(3)
node5 = root.left = TreeNode(5)
root.left.left = TreeNode(6)
root.left.right = TreeNode(2)
root.left.right.left = TreeNode(7)
node4 = root.left.right.right = TreeNode(4)
node1 = root.right = TreeNode(1)
root.right.left = TreeNode(0)
root.right.right = TreeNode(8)
print(root)

s = Solution()
print(root == s.lowestCommonAncestor(root, node5, node1))
print(node5 == s.lowestCommonAncestor(root, node5, node4))
