#   https://www.interviewcake.com/question/python/linked-list-cycles


class LinkedListNode:
    def __init__(self, value):
        self.value = value
        self.next = None


def contains_cycle(node):
    if node is None:
        return False

    step1 = node
    step2 = node.next
    if step2 is None:
        return False

    while step1 is not None and step2 is not None:
        if step1.value == step2.value:
            return True

        step1 = step1.next
        step2 = step2.next.next
    return False


from ListNode import ListNode


class Solution:
    #   https://leetcode.com/explore/challenge/card/february-leetcoding-challenge-2021/584/week-1-february-1st-february-7th/3627
    #   runtime; 76ms, 11.77%
    #   memory; 17.2MB, 67.44%
    def hasCycle(self, head: ListNode) -> bool:
        if head is None:
            return False
        s, f = head, head.next
        while s and f:
            if s == f:
                return True
            s = s.next
            if f.next is None:
                return False
            f = f.next.next
        return False


s = Solution()
head1 = ListNode(3)
head1.next = ListNode(2)
head1.next.next = ListNode(0)
head1.next.next.next = ListNode(-4)
head1.next.next.next.next = head1.next
head2 = ListNode(1)
head2.next = ListNode(2)
head2.next.next = head2
head3 = ListNode(1)
data = [(head1, True),
        (head2, True),
        (head3, False),
        ]
for head, expect in data:
    real = s.hasCycle(head)
    print(f'{head.val} expect {expect} real {real} result {expect == real}')
