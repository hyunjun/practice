#   https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii

#   https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/solution


from ListNode import ListNode
from collections import Counter


class Solution:

    #   https://leetcode.com/explore/challenge/card/january-leetcoding-challenge-2021/579/week-1-january-1st-january-7th/3593
    #   runtime; 44ms, 41.70%
    #   memory; 14.4MB
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head is None:
            return None
        c, vals = Counter(), []
        n = head
        while n:
            c[n.val] += 1
            vals.append(n.val)
            n = n.next
        vals = [val for val in vals if c[val] == 1]
        if 0 == len(vals):
            return None
        p, n = None, head
        while 0 < len(vals):
            n.val = vals.pop(0)
            p, n = n, n.next
        p.next = None
        return head


s = Solution()

l1 = ListNode(1)
l1.next = ListNode(2)
l1.next.next = ListNode(3)
l1.next.next.next = ListNode(3)
l1.next.next.next.next = ListNode(4)
l1.next.next.next.next.next = ListNode(4)
l1.next.next.next.next.next.next = ListNode(5)
print(l1)
head = s.deleteDuplicates(l1)
print(head)

l2 = ListNode(1)
l2.next = ListNode(1)
l2.next.next = ListNode(1)
l2.next.next.next = ListNode(2)
l2.next.next.next.next = ListNode(3)
print(l2)
head = s.deleteDuplicates(l2)
print(head)

l3 = ListNode(1)
l3.next = ListNode(2)
l3.next.next = ListNode(2)
l3.next.next.next = ListNode(2)
print(l3)
head = s.deleteDuplicates(l3)
print(head)

l4 = ListNode(1)
l4.next = ListNode(1)
print(l4)
head = s.deleteDuplicates(l4)
print(head)
