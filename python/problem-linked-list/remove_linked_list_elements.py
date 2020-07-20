#   https://leetcode.com/problems/remove-linked-list-elements


from ListNode import ListNode


class Solution(object):
    #   18.37%
    def removeElements0(self, head, val):
        if head is None:
            return head
        prev, cur = head, head.next
        while prev and val == prev.val:
            prev = prev.next
            head = prev
            if prev:
                cur = prev.next
        while cur:
            if val == cur.val:
                prev.next = cur.next
            else:
                prev = cur
            cur = cur.next
        return head

    #   https://leetcode.com/explore/featured/card/july-leetcoding-challenge/546/week-3-july-15th-july-21st/3396
    #   runtime; 72ms, 73.47%
    #   memory; 16.8MB, 68.52%
    def removeElements1(self, head: ListNode, val: int) -> ListNode:
        nodes, n = [], head
        while n:
            if n.val != val:
                nodes.append(n)
            n = n.next
        if 0 == len(nodes):
            return None
        for i, n in enumerate(nodes):
            if 0 == i:
                continue
            nodes[i - 1].next = n
        nodes[-1].next = None
        return nodes[0]

    #   runtime; 72ms, 73.47%
    #   memory; 16.8MB, 68.52%
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        vals, n = [], head
        while n:
            if n.val != val:
                vals.append(n.val)
            n = n.next
        if 0 == len(vals):
            return None
        p, n = None, head
        for v in vals:
            n.val = v
            p, n = n, n.next
        p.next = None
        return head


s = Solution()
h1 = ListNode(1)
h1.next = ListNode(2)
h1.next.next = ListNode(6)
h1.next.next.next = ListNode(3)
h1.next.next.next.next = ListNode(4)
h1.next.next.next.next.next = ListNode(5)
h1.next.next.next.next.next.next = ListNode(6)
h2 = ListNode(1)
h3 = ListNode(1)
h3.next = ListNode(2)
h3.next.next = ListNode(2)
h3.next.next.next = ListNode(1)
data = [(h1, 6),
        (h2, 1),
        (h3, 2),
        ]
for head, val in data:
    print(f'{head} {val}')
    real = s.removeElements(head, val)
    print(f'\t{real}')
