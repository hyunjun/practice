#   https://leetcode.com/problems/remove-duplicates-from-sorted-list
#   100.00%


from ListNode import ListNode


class Solution:
    def deleteDuplicates(self, head):
        if head is None:
            return None
        prev = head
        cur = prev.next
        while prev is not None and cur is not None:
            if prev.val == cur.val:
                prev.next = cur.next
            else:
                prev = cur
            cur = cur.next
        return head


s = Solution()

l1 = ListNode(1)
l1.next = ListNode(1)
l1.next.next = ListNode(2)
print(l1)
head = s.deleteDuplicates(l1)
print(head)

l2 = ListNode(1)
l2.next = ListNode(1)
l2.next.next = ListNode(2)
l2.next.next.next = ListNode(3)
l2.next.next.next.next = ListNode(3)
print(l2)
head = s.deleteDuplicates(l2)
print(head)
