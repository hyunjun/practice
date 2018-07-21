#   https://leetcode.com/problems/maximum-depth-of-n-ary-tree

#   https://leetcode.com/problems/maximum-depth-of-n-ary-tree/discuss/148882/Python-5-lines-BFS-solution-beats-100-66-ms-faster-than-fastest-!

class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children


class Solution(object):
    #   69.09%
    def maxDepth(self, root):
        if root is None:
            return 0
        maxDepth, queue = 0, [(root, 1)]
        while queue:
            cur, depth = queue.pop(0)
            maxDepth = max(maxDepth, depth)
            if cur.children:
                for child in cur.children:
                    queue.append((child, depth + 1))
        return maxDepth


s = Solution()
node5 = Node(5, None)
node6 = Node(6, None)
node4 = Node(4, None)
node3 = Node(3, [node5, node6])
node2 = Node(2, None)
root = Node(1, [node3, node2, node4])
print(s.maxDepth(root))
