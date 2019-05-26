#   https://leetcode.com/problems/reverse-nodes-in-k-group


from ListNode import ListNode


class Solution:
    #   runtime; 52ms, 94.20%
    #   memory; 14MB, 81.45%
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if head is None:
            return head
        fst, snd, stack = head, head, []
        while fst and snd:
            cnt = 0
            while cnt < k and fst:
                stack.append(fst.val)
                fst = fst.next
                cnt += 1
            if k == len(stack):
                while stack:
                    snd.val = stack.pop()
                    snd = snd.next
        return head


s = Solution()

head1 = ListNode(1)
head1.next = ListNode(2)
head1.next.next = ListNode(3)
head1.next.next.next = ListNode(4)
head1.next.next.next.next = ListNode(5)
print(head1)
print(s.reverseKGroup(head1, 2))

head2 = ListNode(1)
head2.next = ListNode(2)
head2.next.next = ListNode(3)
head2.next.next.next = ListNode(4)
head2.next.next.next.next = ListNode(5)
print(head2)
print(s.reverseKGroup(head2, 3))
