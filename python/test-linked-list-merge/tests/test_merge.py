from merge import *


def test_list_len():
    head = None
    assert list_len(head) == 0

    head = Node(0)
    assert list_len(head) == 1

    head = Node(0)
    head._next = Node(1)
    head._next._next = Node(2)
    assert list_len(head) == 3


def test_merge_case_none():
    head1 = None
    head2 = None
    assert merge(head1, head2) is None

    head1 = None
    head2 = Node(0)
    head2._next = Node(2)
    assert merge(head1, head2) is head2

    head1 = Node(0)
    head1._next = Node(1)
    head1._next._next = Node(3)
    head2 = None
    assert merge(head1, head2) is head1


def test_merge():
    head1 = Node(0)
    head2 = Node(0)
    assert list_len(merge(head1, head2)) == 2

    head1 = Node(0)
    head1._next = Node(1)
    head1._next._next = Node(1)
    head1._next._next._next = Node(3)
    head2 = Node(0)
    head2._next = Node(2)
    merged = merge(head1, head2)
    assert list_len(merged) == 6
    assert merged._next._next._next._next._next._data == 3
