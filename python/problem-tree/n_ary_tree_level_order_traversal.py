#   https://leetcode.com/problems/n-ary-tree-level-order-traversal


class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children


class Solution:
    #   74.44%
    def levelOrder(self, root):
        if root is None:
            return []
        preLevel, queue, res = -1, [(root, 0)], []
        while queue:
            cur, level = queue.pop(0)
            if preLevel != level:
                res.append([cur.val])
                preLevel = level
            else:
                res[-1].append(cur.val)
            for child in cur.children:
                if child:
                    queue.append((child, level + 1))
        return res


s = Solution()
child00 = Node(5, [])
child01 = Node(6, [])
child0 = Node(3, [child00, child01])
child1 = Node(2, [])
child2 = Node(4, [])
root = Node(1, [child0, child1, child2])
print(s.levelOrder(root))
