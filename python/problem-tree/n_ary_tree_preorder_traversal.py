#   https://leetcode.com/problems/n-ary-tree-preorder-traversal

#   https://leetcode.com/problems/n-ary-tree-preorder-traversal/discuss/148867/Python-short-iterative-solution-beats-100-66-ms-faster-than-fastest-!


class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children


class Solution:
    def preorder0(self, root):
        res = []
        def _preorder(node):
            res.append(node.val)
            for child in node.children:
                if child:
                    _preorder(child)
        _preorder(root)
        return res

    #   76.56%
    def preorder(self, root):
        if root is None:
            return []
        stack, res = [root], []
        while stack:
            cur = stack.pop()
            res.append(cur.val)
            for child in cur.children[::-1]:
                if child:
                    stack.append(child)
        return res


s = Solution()
child00 = Node(5, [])
child01 = Node(6, [])
child0 = Node(3, [child00, child01])
child1 = Node(2, [])
child2 = Node(4, [])
root = Node(1, [child0, child1, child2])
print(s.preorder0(root))
print(s.preorder(root))
