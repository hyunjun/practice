#   https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii


from collections import defaultdict


"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    #   https://leetcode.com/explore/challenge/card/december-leetcoding-challenge/569/week-1-december-1st-december-7th/3556
    #   runtime; 48ms, 67.71%
    #   memory; 15.4MB, 18.32%
    def connect(self, root: 'Node') -> 'Node':
        if root is None:
            return root
        q, d = [(root, 1)], defaultdict(list)
        while q:
            node, depth = q.pop(0)
            d[depth].append(node)
            if node.left:
                q.append((node.left, depth + 1))
            if node.right:
                q.append((node.right, depth + 1))
        for nodes in d.values():
            for i, n in enumerate(nodes):
                if i == 0:
                    continue
                nodes[i - 1].next = n
        return root
