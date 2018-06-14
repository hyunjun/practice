#   https://leetcode.com/problems/symmetric-tree


from TreeNode import TreeNode


class Solution:
    def isSymmetric(self, root):
        if root is None:
            return True
        #return self.isSymmetricRecur(root.left, root.right)
        return self.isSymmetricIter(root)

    #   100.00%
    def isSymmetricRecur(self, lNode, rNode):
        if lNode is None and rNode is None:
            return True
        if lNode is None or rNode is None:
            return False
        if lNode.val != rNode.val:
            return False
        return self.isSymmetricRecur(lNode.left, rNode.right) and self.isSymmetricRecur(lNode.right, rNode.left)

    #   84.50%
    def isSymmetricIter(self, root):
        if root is None:
            return True

        queue, prevLevel, levelQueueDict = [(root, 0)], 0, {}
        while queue:
            cur, curLevel = queue[0]
            del queue[0]
            if curLevel not in levelQueueDict:
                levelQueueDict[curLevel] = []
            if 0 < curLevel and 1 < curLevel - prevLevel:
                prevLevel += 1
                prevLevelVals = levelQueueDict[prevLevel]
                prevLevelLen = len(prevLevelVals)
                if prevLevelLen % 2 != 0:
                    return False
                mid = prevLevelLen // 2
                print('{} -> {} vs. {}'.format(prevLevelVals, prevLevelVals[:mid], prevLevelVals[prevLevelLen - 1:mid - 1:-1]))
                if prevLevelVals[:mid] != prevLevelVals[prevLevelLen - 1:mid - 1:-1]:
                    return False
            if cur:
                levelQueueDict[curLevel].append(cur.val)
                queue.append((cur.right, curLevel + 1))
                queue.append((cur.left, curLevel + 1))
            else:
                levelQueueDict[curLevel].append(' ')
        return True


s = Solution()

r = TreeNode(1)
r.left = TreeNode(2)
r.right = TreeNode(2)
r.left.left = TreeNode(3)
r.left.left.left = TreeNode(5)
r.left.right = TreeNode(4)
r.right.left = TreeNode(4)
r.right.right = TreeNode(3)
r.right.right.right = TreeNode(5)
print(s.isSymmetric(r))

r = TreeNode(1)
r.left = TreeNode(2)
r.right = TreeNode(2)
r.left.right = TreeNode(3)
r.right.right = TreeNode(3)
print(s.isSymmetric(r))

r = TreeNode(1)
r.left = TreeNode(2)
r.right = TreeNode(3)
r.left.left = TreeNode(3)
r.right.left = TreeNode(2)
print(s.isSymmetric(r))

r = TreeNode(1)
r.left = TreeNode(2)
r.right = TreeNode(2)
r.left.left = TreeNode(3)
r.left.left.right = TreeNode(5)
r.left.right = TreeNode(4)
r.right.left = TreeNode(4)
r.right.right = TreeNode(3)
r.right.right.right = TreeNode(5)
print(s.isSymmetric(r))

r = TreeNode(5)
r.left = TreeNode(4)
r.left.right = TreeNode(1)
r.left.right.left = TreeNode(2)
r.right = TreeNode(1)
r.right.right = TreeNode(4)
r.right.right.left = TreeNode(2)
print(s.isSymmetric(r))
