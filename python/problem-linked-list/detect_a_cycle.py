#   https://www.hackerrank.com/challenges/ctci-linked-list-cycle


class Node:
    def __init__(self, data = None, next_node = None):
        self.data = data
        self.next = next_node


def has_cycle(head):
    if head is None or head.next is None:
        return False
    s, f = head, head.next
    while s is not None and f is not None and s.data != f.data:
        s = s.next
        if f.next is None:
            return False
        f = f.next.next
    return True


print(has_cycle(None) == False)
print(has_cycle(Node(1)) == False)
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = head.next
print(has_cycle(head) == True)
