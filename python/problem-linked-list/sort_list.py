#   https://leetcode.com/problems/sort-list

#   https://leetcode.com/problems/sort-list/discuss/453171/Python-Merge-Sort-Constant-Space-and-O(nlogn)-time


from ListNode import ListNode


class Solution:
    #   runtime; 144ms, 86.09%
    #   memory; 19.6MB, 100.00%
    def sortList0(self, head: ListNode) -> ListNode:
        if head is None:
            return None
        node, vals = head, []
        while node:
            vals.append(node.val)
            node = node.next
        vals.sort()
        node = head
        while node:
            node.val = vals.pop(0)
            node = node.next
        return head

    #   runtime; 96ms, 95.78%
    #   memory; 19.8MB, 100.00%
    def sortList1(self, head: ListNode) -> ListNode:
        if head is None:
            return None
        node, nodes = head, []
        while node:
            nodes.append(node)
            node = node.next
        nodes.sort(key=lambda n: n.val)
        for i in range(len(nodes) - 1):
            nodes[i].next = nodes[i + 1]
        nodes[-1].next = None
        return nodes[0]

    #   https://leetcode.com/explore/challenge/card/october-leetcoding-challenge/560/week-2-october-8th-october-14th/3493
    #   runtime; 80ms, 99.30%
    #   memory; 21.4MB
    def sortList(self, head: ListNode) -> ListNode:
        n, vals = head, []
        while n:
            vals.append(n.val)
            n = n.next
        vals.sort()
        n = head
        for val in vals:
            n.val = val
            n = n.next
        return head


s = Solution()
head1 = ListNode(4)
head1.next = ListNode(2)
head1.next.next = ListNode(1)
head1.next.next.next = ListNode(3)
rHead1 = ListNode(1)
rHead1.next = ListNode(2)
rHead1.next.next = ListNode(3)
rHead1.next.next.next = ListNode(4)
head2 = ListNode(-1)
head2.next = ListNode(5)
head2.next.next = ListNode(3)
head2.next.next.next = ListNode(4)
head2.next.next.next.next = ListNode(0)
rHead2 = ListNode(-1)
rHead2.next = ListNode(0)
rHead2.next.next = ListNode(3)
rHead2.next.next.next = ListNode(4)
rHead2.next.next.next.next = ListNode(5)
data = [(head1, rHead1),
        (head2, rHead2),
        ]
for head, expected in data:
    real = s.sortList(head)
    print(f'expected {expected} real {real}')
