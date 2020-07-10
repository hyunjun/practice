#   https://leetcode.com/problems/flatten-a-multilevel-doubly-linked-list


class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child


class Solution:
    #   https://leetcode.com/explore/featured/card/july-leetcoding-challenge/545/week-2-july-8th-july-14th/3386
    #   runtime; 48ms, 28.95%
    #   memory; 14.5MB, 25.85%
    def flatten(self, head: 'Node') -> 'Node':
        if head is None:
            return head

        res, stack = [], [head]
        while stack:
            node = stack.pop()
            res.append(node)
            if node.next:
                stack.append(node.next)
            if node.child:
                stack.append(node.child)
        for i, r in enumerate(res):
            if i == 0:
                r.prev = r.child = None
                continue
            res[i - 1].next = r
            r.prev = res[i - 1]
            r.child = None
        res[-1].next = res[-1].child = None
    
        return res[0]


nodes = [Node(i, None, None, None) for i in range(1, 13)]
for s, e in [(0, 6), (6, 10), (10, 12)]:
    for i in range(s, e):
        if i == s:
            continue
        nodes[i - 1].next = nodes[i]
        nodes[i].prev = nodes[i - 1]
nodes[2].child = nodes[6]
nodes[7].child = nodes[10]


s = Solution()
s.flatten(nodes[0])
