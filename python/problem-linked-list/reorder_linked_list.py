#   https://aonecode.com/aplusplus/interviewctrl/getInterview/203


from ListNode import ListNode


def reorder0(head):
    if head is None:
        return None

    c, l = head, []
    while c:
        l.append(c)
        c = c.next

    i1, i2, c, n = 0, len(l) - 1, None, None
    for i in range(len(l)):
        if i % 2 == 0:
            c, n = l[i1], l[i2]
            c.next = n
            i1 += 1
        else:
            c, n = l[i2], l[i1]
            c.next = n
            i2 -= 1
    for i in l:
        print(i.val)
    return l[0]


def reorder(head):
    if head is None:
        return None

    c, l = head, []
    while c:
        l.append(c.val)
        c = c.next

    i1, i2, c = 0, len(l) - 1, head
    for i in range(len(l)):
        if i % 2 == 0:
            if 0 < i:
                c.val = l[i1]
            i1 += 1
        else:
            c.val = l[i2]
            i2 -= 1
        c = c.next
    return head


head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
print(head)
print(reorder(head))
