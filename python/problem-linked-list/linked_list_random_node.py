#   https://leetcode.com/problems/linked-list-random-node


from ListNode import ListNode
import random


#   https://leetcode.com/explore/challenge/card/december-leetcoding-challenge/569/week-1-december-1st-december-7th/3552
#   runtime; 76ms, 84.39%
#   memory; 17.5MB, 10.13%
class Solution:

    def __init__(self, head: ListNode):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        """
        self.nodes, node = [], head
        while node:
            self.nodes.append(node)
            node = node.next

    def getRandom(self) -> int:
        """
        Returns a random node's value.
        """
        if 0 < len(self.nodes):
            return random.choice(self.nodes).val
        return float('inf')


head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
s = Solution(head)
print(s.getRandom())
