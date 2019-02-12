#   https://leetcode.com/problems/populating-next-right-pointers-in-each-node


class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None


class Solution:
    #   runtime; 52ms, 52.56%
    #   memory; 15.6MB, 0.97%
    def connect(self, root):
        if root is None:
            return
        prevLv, prev, q = 0, None, [(1, root)]
        while q:
            lv, node = q.pop(0)
            if prevLv == lv:
                prev.next = node
            prevLv, prev = lv, node
            if node.left:
                q.append((lv + 1, node.left))
            if node.right:
                q.append((lv + 1, node.right))


s = Solution()
root = TreeLinkNode(1)
root.left = TreeLinkNode(2)
root.right = TreeLinkNode(3)
root.left.left = TreeLinkNode(4)
root.left.right = TreeLinkNode(5)
root.right.left = TreeLinkNode(6)
root.right.right = TreeLinkNode(7)
s.connect(root)
