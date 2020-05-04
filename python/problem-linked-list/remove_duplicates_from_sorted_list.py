#   https://leetcode.com/problems/remove-duplicates-from-sorted-list
#   100.00%

#   https://www.hackerrank.com/challenges/delete-duplicate-value-nodes-from-a-sorted-linked-list


def removeDuplicates(head):
    n = head
    while n and n.next:
        if n.data == n.next.data:
            n.next = n.next.next
        else:
            n = n.next
    return head


from ListNode import ListNode


class Solution:
    #   runtime; 48ms
    def deleteDuplicates0(self, head):
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

    #   runtime; 40ms, 75.43%
    #   memory; 13.9MB, 6.45%
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head is None:
            return None
        p = n = head
        while n:
            if p.val != n.val:
                p.next = n
                p = n
            n = n.next
        p.next = None
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
