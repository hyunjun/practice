#   https://leetcode.com/problems/linked-list-cycle-ii


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        if self.next:
            return '{} -> {}'.format(self.val, self.next)
        return '{} -> X'.format(self.val)


class Solution:
    def detectCycleFailed(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return None
        sprev = slow = fprev = head
        fast = head.next
        print('before sprev {}, slow {}, fprev {}, fast {}'.format(sprev.val, slow.val, fprev.val, fast.val))
        while slow and fast:
            if sprev is fprev and slow is fast:
                return sprev
            sprev = slow
            slow = slow.next
            if fast.next is None:
                return None
            fprev = fast.next
            fast = fast.next.next
            print('       sprev {}, slow {}, fprev {}, fast {}'.format(sprev.val, slow.val, fprev.val, fast.val))
        return None

    #   17.86%
    def detectCycle(self, head):
        if head is None or head.next is None:
            return None
        s = set()
        cur = head
        while cur and cur not in s:
            s.add(cur)
            cur = cur.next
            if cur in s:
                return cur
        return None


s = Solution()

head = ListNode(3)
head.next = ListNode(2)
head.next.next = ListNode(0)
head.next.next.next = ListNode(-4)
head.next.next.next.next = head.next
print('3 -> 2 -> 0 -> -4 -> 2')
print(s.detectCycle(head).val)

head = ListNode(-1)
head.next = ListNode(-7)
head.next.next = ListNode(7)
head.next.next.next = ListNode(-4)
head.next.next.next.next = ListNode(19)
head.next.next.next.next.next = ListNode(6)
head.next.next.next.next.next.next = ListNode(-9)
head.next.next.next.next.next.next.next = ListNode(-5)
head.next.next.next.next.next.next.next.next = ListNode(-2)
head.next.next.next.next.next.next.next.next.next = ListNode(-5)
head.next.next.next.next.next.next.next.next.next.next = head.next.next.next.next.next.next.next.next.next
print('-1 -> -7 -> 7 -> -4 -> 19 -> 6 -> -9 -> -5 -> -2 -> -5 -> -5 (9th)')
print(s.detectCycle(head).val)
