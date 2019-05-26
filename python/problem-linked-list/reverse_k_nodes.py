#   https://www.youtube.com/watch?v=qGSi6-gmCAg

#   https://www.geeksforgeeks.org/reverse-a-list-in-groups-of-given-size
#   https://www.geeksforgeeks.org/reverse-alternate-k-nodes-in-a-singly-linked-list


from ListNode import ListNode


def reverseKNodes(head, k):
    if head is None:
        return head
    fst, snd, stack = head, head, []
    while fst and snd:
        cnt = 0
        while cnt < k and fst:
            stack.append(fst.val)
            fst = fst.next
            cnt += 1
        while stack:
            snd.val = stack.pop()
            snd = snd.next
    return head


head1 = ListNode(1)
head1.next = ListNode(2)
head1.next.next = ListNode(3)
head1.next.next.next = ListNode(4)
head1.next.next.next.next = ListNode(5)
head1.next.next.next.next.next = ListNode(6)
head1.next.next.next.next.next.next = ListNode(7)
head1.next.next.next.next.next.next.next = ListNode(8)
print(head1)
print(reverseKNodes(head1, 3))
print(reverseKNodes(ListNode(1), 3))

head2 = ListNode(1)
head2.next = ListNode(2)
head2.next.next = ListNode(3)
head2.next.next.next = ListNode(4)
head2.next.next.next.next = ListNode(5)
print(head2)
print(reverseKNodes(head2, 2))

head3 = ListNode(1)
head3.next = ListNode(2)
head3.next.next = ListNode(3)
head3.next.next.next = ListNode(4)
head3.next.next.next.next = ListNode(5)
print(head3)
print(reverseKNodes(head3, 3))
