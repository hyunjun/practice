#   https://leetcode.com/problems/copy-list-with-random-pointer


from collections import defaultdict


# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

    def __repr__(self):
        return f'{self.val} -> {self.next}'


class Solution:
    #   https://leetcode.com/explore/challenge/card/february-leetcoding-challenge-2021/585/week-2-february-8th-february-14th/3635
    #   runtime; 36ms, 68.57%
    #   memory; 15.1MB, 29.95%
    def copyRandomList(self, head: 'Node') -> 'Node':
        if head is None:
            return None
        newHead, prev, node, i, idxDict, nodeDict, newNodeDict = None, None, head, 0, defaultdict(), defaultdict(), defaultdict()
        while node:
            newNode = Node(node.val)
            newNodeDict[i] = newNode
            idxDict[id(node)] = i
            if node.random:
                nodeDict[i] = id(node.random)
            if newHead is None:
                newHead = newNode
            if prev:
                prev.next = newNode
            prev, node = newNode, node.next
            i += 1
        node, cur, i = newHead, head, 0
        while node:
            if i in nodeDict:
                randomIdx = idxDict[nodeDict[i]]
                node.random = newNodeDict[randomIdx]
            node = node.next
            cur = cur.next
            i += 1
        return newHead


s = Solution()
head1 = Node(7)
head1.next = Node(13)
head1.next.next = Node(11)
head1.next.next.next = Node(10)
head1.next.next.next.next = Node(1)
head1.next.random = head1
head1.next.next.random = head1.next.next.next.next
head1.next.next.next.random = head1.next.next
head1.next.next.next.next.random = head1.next.next
head2 = Node(1)
head2.next = Node(2)
head2.random = head2.next
head2.next.random = head2.next
head3 = Node(3)
head3.next = Node(3)
head3.next.next = Node(3)
head3.next.random = head3
for head in [head1, head2, head3, None]:
    print(head)
    real = s.copyRandomList(head)
    print(real)
