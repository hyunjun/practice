#   https://leetcode.com/problems/n-ary-tree-postorder-traversal

#   https://leetcode.com/problems/n-ary-tree-postorder-traversal/discuss/148880/Python-6-lines-BFS-solution-beats-100-77-ms-faster-than-fastest-!


class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children


class Solution:
    def postorder0(self, root):
        res = []
        def _postorder(node):
            for child in node.children:
                if child:
                    _postorder(child)
            res.append(node.val)
        _postorder(root)
        return res

    #   53.07%
    def postorder(self, root):
        if root is None:
            return []
        stack, res = [root], []
        while stack:
            cur = stack.pop()
            res.append(cur.val)
            for child in cur.children:
                if child:
                    stack.append(child)
        return res[::-1]


s = Solution()
child00 = Node(5, [])
child01 = Node(6, [])
child0 = Node(3, [child00, child01])
child1 = Node(2, [])
child2 = Node(4, [])
root = Node(1, [child0, child1, child2])
print(s.postorder0(root))
print(s.postorder(root))
