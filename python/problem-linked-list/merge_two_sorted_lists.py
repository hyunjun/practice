#   https://leetcode.com/problems/merge-two-sorted-lists
#   99.95%


from ListNode import ListNode


class Solution:
    def mergeTwoLists(self, l1, l2):
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        head = cur = l2
        if l1.val < l2.val:
            head = cur = l1
            c1, c2 = l1.next, l2
        else:
            c1, c2 = l1, l2.next
        while c1 is not None and c2 is not None:
            if c1.val < c2.val:
                cur.next = c1
                c1 = c1.next
            else:
                cur.next = c2
                c2 = c2.next
            cur = cur.next
        while c1 is not None:
            cur.next = c1
            c1 = c1.next
            cur = cur.next
        while c2 is not None:
            cur.next = c2
            c2 = c2.next
            cur = cur.next
        return head


s = Solution()
l1 = ListNode(1)
l1.next = ListNode(2)
l1.next.next = ListNode(4)
print(l1)
l2 = ListNode(1)
l2.next = ListNode(3)
l2.next.next = ListNode(4)
print(l2)
head = s.mergeTwoLists(l1, l2)
print(head)
