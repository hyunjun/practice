#   https://leetcode.com/problems/same-tree


from TreeNode import TreeNode


class Solution:
    #   98.97%
    def isSameTree0(self, p, q):
        pQueue = [p]
        qQueue = [q]
        while 0 < len(pQueue) and 0 < len(qQueue):
            l, r = pQueue[0], qQueue[0]
            del pQueue[0]
            del qQueue[0]
            if l is None and r is not None or l is not None and r is None:
                return False
            if l is not None and r is not None and l.val != r.val:
                return False
            if l is not None:
                pQueue.append(l.left)
                pQueue.append(l.right)
            if r is not None:
                qQueue.append(r.left)
                qQueue.append(r.right)
        return True

    #   https://leetcode.com/explore/featured/card/july-leetcoding-challenge/545/week-2-july-8th-july-14th/3389
    #   runtime; 32ms, 60.40%
    #   memory; 13.8MB, 76.71%
    def isSameTree1(self, p: TreeNode, q: TreeNode) -> bool:

        def isSameNode(l, r):
            if not l and not r:
                return True
            if l and r and l.val == r.val:
                return isSameNode(l.left, r.left) and isSameNode(l.right, r.right)
            return False

        return isSameNode(p, q)

    #   runtime; 68ms
    #   memory; 13.6MB, 93.71%
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:

        pNode, pStack, qNode, qStack = p, [], q, []
        while (pNode or pStack) and (qNode or qStack):
            if pNode and qNode:
                pStack.append(pNode)
                qStack.append(qNode)
                pNode, qNode = pNode.left, qNode.left
            elif not pNode and not qNode and pStack and qStack:
                pNode, qNode = pStack.pop(), qStack.pop()
                if pNode and qNode and pNode.val == qNode.val:
                    pNode, qNode = pNode.right, qNode.right
                else:
                    return False
            else:
                return False
        return not pNode and not qNode and not pStack and not qStack


s = Solution()
p1 = TreeNode(1)
p1.left = TreeNode(2)
p1.right = TreeNode(3)
q1 = TreeNode(1)
q1.left = TreeNode(2)
q1.right = TreeNode(3)
p2 = TreeNode(1)
p2.left = TreeNode(2)
q2 = TreeNode(1)
q2.right = TreeNode(2)
p3 = TreeNode(1)
p3.left = TreeNode(2)
p3.right = TreeNode(1)
q3 = TreeNode(1)
q3.left = TreeNode(1)
q3.right = TreeNode(2)
data = [(p1, q1, True),
        (p2, q2, False),
        (p3, q3, False),
        (None, TreeNode(0), False),
        ]
for p, q, expect in data:
    real = s.isSameTree(p, q)
    print(f'{p} {q} expect {expect} real {real} result {expect == real}')
