#   https://leetcode.com/problems/subtree-of-another-tree

#   https://leetcode.com/problems/subtree-of-another-tree/solution


from TreeNode import TreeNode


class Solution:
    #   Wrong Answer
    def isSubtree0(self, s, t):
        if s is None and t is None:
            return True
        if s is None or t is None:
            return False

        def dfs(node):
            cur, stack, res = node, [], []
            while cur or stack:
                if cur:
                    stack.append(cur)
                    cur = cur.left
                else:
                    cur = stack.pop()
                    res.append(cur.val)
                    cur = cur.right
            return ''.join([str(r) for r in res])

        sStr, tStr = dfs(s), dfs(t)
        return tStr in sStr

    #   Wrong Answer
    def isSubtree1(self, s, t):
        if s is None and t is None:
            return True
        if s is None or t is None:
            return False

        sames, queue = [], [s]
        while queue:
            cur = queue.pop(0)
            if cur.val == t.val:
                sames.append(cur)
            if cur.left:
                queue.append(cur.left)
            if cur.right:
                queue.append(cur.right)

        if 0 == len(sames):
            return False

        for same in sames:
            queueS, queueT = [same], [t]
            while queueS and queueT:
                curS, curT = queueS.pop(), queueT.pop()
                if curS.val != curT.val:
                    return False
                if curS.left:
                    queueS.append(curS.left)
                if curT.left:
                    queueT.append(curT.left)
                if curS.right:
                    queueS.append(curS.right)
                if curT.right:
                    queueT.append(curT.right)
            if 0 == len(queueS) and 0 == len(queueT):
                return True
        return False

    #   Wrong Answer
    def isSubtree2(self, s, t):
        if s is None and t is None:
            return True
        if s is None or t is None:
            return False

        def dfs(node):
            cur, stack, res = node, [], []
            while cur or stack:
                if cur:
                    stack.append(cur)
                    cur = cur.left
                else:
                    cur = stack.pop()
                    res.append(cur.val)
                    cur = cur.right
            return ''.join([str(r) for r in res])

        sStr, tStr = dfs(s), dfs(t)
        if tStr not in sStr:
            return False

        def edgeDict(node):
            queue, eDict = [(node, None)], {}
            while queue:
                cur, curParent = queue.pop(0)
                if cur.left is None and cur.right is None:
                    if cur.val in eDict:
                        eDict[cur.val].add(curParent.val)
                    else:
                        if curParent is None:
                            eDict[cur.val] = set()
                        else:
                            eDict[cur.val] = set([curParent.val])
                if cur.left:
                    queue.append((cur.left, cur))
                if cur.right:
                    queue.append((cur.right, cur))
            return eDict

        sEDict, tEDict = edgeDict(s), edgeDict(t)
        for nVal, nParentVals in tEDict.items():
            if nVal not in sEDict:
                return False
            for nParentVal in nParentVals:
                if nParentVal not in sEDict[nVal]:
                    return False
        return True

    #   68.98%
    def isSubtree(self, s, t):
        def isSame(l, r):
            if not l and not r:
                return True
            if not l or not r:
                return False
            while l.val == r.val:
                return isSame(l.left, r.left) and isSame(l.right, r.right)
            return False

        cur, stack = s, []
        while cur or stack:
            if cur:
                stack.append(cur)
                cur = cur.left
            else:
                cur = stack.pop()
                if isSame(cur, t):
                    return True
                cur = cur.right
        return False



solution = Solution()

s = TreeNode(3)
s.left = TreeNode(4)
s.right = TreeNode(5)
s.left.left = TreeNode(1)
s.left.right = TreeNode(2)
t = TreeNode(4)
t.left = TreeNode(1)
t.right = TreeNode(2)
print(solution.isSubtree(s, t)) #   True

s = TreeNode(3)
s.left = TreeNode(4)
s.right = TreeNode(5)
s.left.left = TreeNode(1)
s.left.right = TreeNode(2)
s.left.right.left = TreeNode(0)
print(solution.isSubtree(s, t)) #   False

s = TreeNode(3)
s.left = TreeNode(4)
s.right = TreeNode(5)
s.left.left = TreeNode(1)
s.left.right = TreeNode(2)
s.left.left.left = TreeNode(0)
print(solution.isSubtree(s, t)) #   False

s = TreeNode(1)
t = TreeNode(0)
print(solution.isSubtree(s, t)) #   False

s = TreeNode(1)
s.left = TreeNode(1)
t = TreeNode(1)
print(solution.isSubtree(s, t)) #   True

s = TreeNode(1)
s.left = TreeNode(2)
s.right = TreeNode(3)
t = TreeNode(1)
t.left = TreeNode(2)
print(solution.isSubtree(s, t)) #   False

#[1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,2]
#[1,null,1,null,1,null,1,null,1,null,1,2]
