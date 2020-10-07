#   https://leetcode.com/problems/rotate-list


from ListNode import ListNode


class Solution:
    #   https://leetcode.com/explore/challenge/card/october-leetcoding-challenge/559/week-1-october-1st-october-7th/3486
    #   runtime; 36ms, 77.29%
    #   memory; 14.1MB, 13.01%
    def rotateRight0(self, head: ListNode, k: int) -> ListNode:
        if head is None or k == 0:
            return head
        node, vals = head, []
        while node:
            vals.append(node.val)
            node = node.next
        k %= len(vals)
        if len(vals) == 1 or k == 0:
            return head
        vals = vals[-k:] + vals[:len(vals) - k]
        node = head
        for val in vals:
            node.val = val
            node = node.next
        return head

    #   runtime; 36ms, 77.29%
    #   memory; 14.1MB, 17.73%
    def rotateRight1(self, head: ListNode, k: int) -> ListNode:
        if head is None or k == 0:
            return head
        n, listLen = head, 0
        while n:
            n = n.next
            listLen += 1
        k %= listLen
        if k == 0:
            return head
        pkn, kn = None, head
        for _ in range(k):
            pkn = kn
            kn = kn.next
        pn, n = None, head
        while kn:
            pn = n
            n = n.next
            pkn = kn
            kn = kn.next
        pkn.next = head
        pn.next = None
        return n

    #   runtime; 32ms, 92.71%
    #   memory; 13.9MB, 41.03%
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if head is None or k == 0:
            return head
        n, nodes = head, []
        while n:
            nodes.append(n)
            n = n.next
        k %= len(nodes)
        if k == 0:
            return head
        nodes[-(k + 1)].next = None
        nodes[-1].next = nodes[0]
        return nodes[-k]


s = Solution()
head1 = ListNode(1)
head1.next = ListNode(2)
head1.next.next = ListNode(3)
head1.next.next.next = ListNode(4)
head1.next.next.next.next = ListNode(5)
head2 = ListNode(0)
head2.next = ListNode(1)
head2.next.next = ListNode(2)
head3 = ListNode(1)
head4 = ListNode(1)
head4.next = ListNode(2)
data = [(head1, 2),
        (head2, 4),
        (head3, 0),
        (head4, 0),
        (head4, 2),
        ]
for head, k in data:
    print(f'{head}')
    real = s.rotateRight(head, k)
    print(f'\t{real} {k}')
'''
    k = 2
    1   2    3   4   5
pkn kn
    pkn kn
        pkn kn
pn  n
             pkn kn
    pn  n
                 pkn kn
        pn  n
                     pkn kn
            pn  n
'''
