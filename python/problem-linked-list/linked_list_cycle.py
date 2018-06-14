#   https://leetcode.com/problems/linked-list-cycle
#   4.44%

#   https://leetcode.com/problems/linked-list-cycle/solution


from ListNode import ListNode


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
