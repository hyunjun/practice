class Node:
    def __init__(self, data):
        self._data = data
        self._next = None

    def __str__(self):
        return '[{}]'.format(self._data)


def list_len(head):
    if head is None:
        return 0

    cnt, node = 0, head
    while node is not None:
        cnt += 1
        node = node._next
    return cnt


def print_list(head):
    node = head
    while node is not None:
        print node,
        node = node._next
    print


def merge(head1, head2):
    if head1 is None:
        return head2
    if head2 is None:
        return head1

    #   set merged_head which has a smaller data between head1 and head2
    merged, node1, node2 = None, head1, head2
    if node1._data < head2._data:
        merged = Node(node1._data)
        node1 = node1._next
    else:
        merged = Node(node2._data)
        node2 = node2._next
    merged_head = merged

    #   merge two list
    while node1 is not None and node2 is not None:
        if node1._data < node2._data:
            merged._next = Node(node1._data)
            node1 = node1._next
            merged = merged._next
        else:
            merged._next = Node(node2._data)
            node2 = node2._next
            merged = merged._next

    #   merge left-overs
    while node1 is not None:
        merged._next = Node(node1._data)
        node1 = node1._next
        merged = merged._next

    while node2 is not None:
        merged._next = Node(node2._data)
        node2 = node2._next
        merged = merged._next

    return merged_head


if __name__ == '__main__':
    h1 = Node(0)
    h1._next = Node(1)
    h1._next._next = Node(1)
    h1._next._next._next = Node(3)
    h2 = Node(0)
    h2._next = Node(2)
    n = merge(h1, h2)
    print_list(n)
