#   https://leetcode.com/problems/same-tree
#   98.97%


from TreeNode import TreeNode


class Solution:
    def isSameTree(self, p, q):
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


s = Solution()

p = TreeNode(1)
p.left = TreeNode(2)
p.right = TreeNode(3)
q = TreeNode(1)
q.left = TreeNode(2)
q.right = TreeNode(3)
print(s.isSameTree(p, q))

p = TreeNode(1)
p.left = TreeNode(2)
q = TreeNode(1)
q.right = TreeNode(2)
print(s.isSameTree(p, q))

p = TreeNode(1)
p.left = TreeNode(2)
p.right = TreeNode(1)
q = TreeNode(1)
q.left = TreeNode(1)
q.right = TreeNode(2)
print(s.isSameTree(p, q))
