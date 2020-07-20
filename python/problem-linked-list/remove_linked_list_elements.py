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
    def removeElements(self, head: ListNode, val: int) -> ListNode:
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


s = Solution()
h1 = ListNode(1)
h1.next = ListNode(2)
h1.next.next = ListNode(6)
h1.next.next.next = ListNode(3)
h1.next.next.next.next = ListNode(4)
h1.next.next.next.next.next = ListNode(5)
h1.next.next.next.next.next.next = ListNode(6)
print(h1)
node = s.removeElements(h1, 6)
print(node)
node2 = s.removeElements(h1, 1)
print(node2)
h2 = ListNode(1)
node3 = s.removeElements(h2, 1)
print(node3)
h3 = ListNode(1)
h3.next = ListNode(2)
h3.next.next = ListNode(2)
h3.next.next.next = ListNode(1)
print(h3)
node = s.removeElements(h3, 2)
print(node)
