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

    #   isSame 호출 전에 cur.val == t.val 비교를 추가했더니 오히려 느려짐
    #   runtime; 212ms -> 260ms, 71.67%
    #   memory; 14MB, 81.07%
    def isSubtree3(self, s, t):
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
                if cur.val == t.val and isSame(cur, t):
                    return True
                cur = cur.right
        return False

    #   runtime; 108ms, 85.28%
    #   memory; 14.8MB, 7.33%
    def isSubtree(self, s, t):
        def preorder(n):
            if n is None:
                return ''
            return '{},{},{}'.format(n.val, preorder(n.left), preorder(n.right))
        def inorder(n):
            if n is None:
                return ''
            return '{},{},{}'.format(inorder(n.left), n.val, inorder(n.right))
        def postorder(n):
            if n is None:
                return ''
            return '{},{},{}'.format(postorder(n.left), postorder(n.right), n.val)

        preS, preT = preorder(s), preorder(t)
        inS, inT = inorder(s), inorder(t)
        postS, postT = postorder(s), postorder(t)

        return preT in preS and inT in inS and postT in postS


solution = Solution()

s1 = TreeNode(3)
s1.left = TreeNode(4)
s1.right = TreeNode(5)
s1.left.left = TreeNode(1)
s1.left.right = TreeNode(2)
t1 = TreeNode(4)
t1.left = TreeNode(1)
t1.right = TreeNode(2)

s2 = TreeNode(3)
s2.left = TreeNode(4)
s2.right = TreeNode(5)
s2.left.left = TreeNode(1)
s2.left.right = TreeNode(2)
s2.left.right.left = TreeNode(0)

s3 = TreeNode(3)
s3.left = TreeNode(4)
s3.right = TreeNode(5)
s3.left.left = TreeNode(1)
s3.left.right = TreeNode(2)
s3.left.left.left = TreeNode(0)

s4 = TreeNode(1)
t2 = TreeNode(0)

s5 = TreeNode(1)
s5.left = TreeNode(1)
t3 = TreeNode(1)

s6 = TreeNode(1)
s6.left = TreeNode(2)
s6.right = TreeNode(3)
t4 = TreeNode(1)
t4.left = TreeNode(2)

data = [(s1, t1, True),
        (s2, t1, False),
        (s3, t1, False),
        (s4, t2, False),
        (s5, t3, True),
        (s6, t4, False),
        ]
for s, t, expected in data:
    real = solution.isSubtree(s, t)
    print('{}, {}, expected {}, real {}, result {}'.format(s, t, expected, real, expected == real))

#[1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,2]
#[1,null,1,null,1,null,1,null,1,null,1,2]
