#   https://www.hackerrank.com/challenges/find-the-merge-point-of-two-joined-linked-lists


def findMergeNode(head1, head2):
    if head1 is None or head2 is None or head1 == head2:
        return None
    s, n = set(), head1
    while n:
        s.add(n)
        n = n.next
    n = head2
    while n:
        if n in s:
            return n.data
        n = n.next
    return None
