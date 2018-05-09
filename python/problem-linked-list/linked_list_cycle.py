#   https://leetcode.com/problems/linked-list-cycle
#   4.44%

#   https://leetcode.com/problems/linked-list-cycle/solution


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head is None or head.next is None:
            return False
        slow = head
        fast = head.next.next
        while slow and fast:
            if slow is fast:
                return True
            slow = slow.next
            if fast.next is None:
                return False
            fast = fast.next.next
        return False
