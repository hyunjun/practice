#   https://www.hackerrank.com/challenges/reverse-a-doubly-linked-list


class DoublyLinkedListNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


def reverse(head):
    p, c = None, head
    while c:
        n = c.next
        if p:
            p.prev = c
        c.next = p
        if p:
            print(p.data, '<->', c.data)
        else:
            print(p, '<-', c.data)
        p, c = c, n
    return p


head = DoublyLinkedListNode(1)
n1 = DoublyLinkedListNode(2)
n2 = DoublyLinkedListNode(3)
n3 = DoublyLinkedListNode(4)
head.next = n1
n1.prev = head
n1.next = n2
n2.prev = n1
n2.next = n3
n3.prev = n2

n = head
while n:
    print(n.data)
    n = n.next

n = reverse(head)
while n:
    print(n.data)
    n = n.next
