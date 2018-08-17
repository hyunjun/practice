#   https://www.youtube.com/watch?v=7HgsS8bRvjo


from TreeNode import TreeNode


class Solution:
    def numOfUniversalValueTreeRecur(self, root):
        self.ans = 0
        def isUniversalValueTree(node):
            if node is None:
                return True
            if node and node.left is None and node.right is None:
                self.ans += 1
                return True
            lRet, rRet = isUniversalValueTree(node.left), isUniversalValueTree(node.right)
            if lRet and rRet and ((node.left and node.right and node.left.val == node.right.val == node.val) or (node.left and node.right is None and node.left.val == node.val) or (node.left is None and node.right and node.right.val == node.val)):
                self.ans += 1
                return True
            return False
        isUniversalValueTree(root)
        return self.ans

    def numOfUniversalValueTree(self, root):
        if root is None:
            return 0
        ret, queue, parentResultDict = 0, [(root, 0, None)], {}
        while queue:
            cur, idx, result = queue.pop(0)
            if cur.left is None and cur.right is None:
                parentResultDict[idx] = (cur.val, True)
                ret += 1
            else:
                parentResultDict[idx] = (cur.val, result)
                if cur.left:
                    queue.append((cur.left, 2 * idx + 1, None))
                if cur.right:
                    queue.append((cur.right, 2 * idx + 2, None))
        for idx, (nodeVal, result) in parentResultDict.items():
            if result:
                continue
            curResult, lChildKey, rChildKey = False, 2 * idx + 1, 2 * idx + 2
            if lChildKey in parentResultDict and rChildKey in parentResultDict:
                lChildVal, lRet = parentResultDict[lChildKey]
                rChildVal, rRet = parentResultDict[rChildKey]
                if lRet and rRet and lChildVal == nodeVal == rChildVal:
                    ret += 1
                    curResult = True
            elif lChildKey in parentResultDict and rChildKey not in parentResultDict:
                lChildVal, lRet = parentResultDict[lChildKey]
                if lRet and lChildVal == nodeVal:
                    ret += 1
                    curResult = True
            elif lChildKey not in parentResultDict and rChildKey in parentResultDict:
                rChildVal, rRet = parentResultDict[rChildKey]
                if rRet and nodeVal == rChildVal:
                    ret += 1
                    curResult = True
            parentResultDict[idx] = (nodeVal, curResult)
        return ret


s = Solution()
print(s.numOfUniversalValueTree(None) == 0)

'''
        0
       / \
 O -> 1   0
         / \
   O -> 1   0 <- O
       / \
 O -> 1   1 <- O
'''
root = TreeNode(0)
root.left = TreeNode(1)
root.right = TreeNode(0)
root.right.left = TreeNode(1)
root.right.left.left = TreeNode(1)
root.right.left.right = TreeNode(1)
root.right.right = TreeNode(0)
print(s.numOfUniversalValueTree(root) == 5)

'''
        0
       /
 O -> 1
'''
root = TreeNode(0)
root.left = TreeNode(1)
print(s.numOfUniversalValueTree(root) == 1)

'''
          0
         / \
   O -> 1   0 <- O
       /
 O -> 1
'''
root = TreeNode(0)
root.left = TreeNode(1)
root.right = TreeNode(0)
root.left.left = TreeNode(1)
print(s.numOfUniversalValueTree(root) == 3)
