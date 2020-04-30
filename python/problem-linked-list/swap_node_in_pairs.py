#   https://leetcode.com/problems/swap-nodes-in-pairs

#   https://leetcode.com/problems/swap-nodes-in-pairs/discuss/158034/python-easy-to-understand-method-beats-100


from ListNode import ListNode


class Solution:
    #   42.74%
    def swapPairs(self, head):
        prev = None
        cur = head
        n = cur.next if cur else None
        ret = None
        while cur and n:
            if ret is None:
                ret = n
            nn = n.next
            if prev:
                prev.next = n
            cur.next = nn
            n.next = cur
            prev = cur
            cur = nn
            n = cur.next if cur else None
        if ret:
            return ret
        return head

    #   https://leetcode.com/explore/featured/card/recursion-i/250/principle-of-recursion/1681
    #   runtime; 20ms, 98.23%
    #   memory; 13.7MB
    def swapPairs(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head
        c, n = head, head.next
        while c and n:
            c.val, n.val = n.val, c.val
            if n.next and n.next.next:
                c = n.next
                n = n.next.next
            else:
                break
        return head


s = Solution()
print(s.swapPairs(None))
print(s.swapPairs(ListNode(1)))
h1 = ListNode(1)
h1.next = ListNode(2)
print(s.swapPairs(h1))
h2 = ListNode(1)
h2.next = ListNode(2)
h2.next.next = ListNode(3)
print(s.swapPairs(h2))
h3 = ListNode(1)
h3.next = ListNode(2)
h3.next.next = ListNode(3)
h3.next.next.next = ListNode(4)
print(s.swapPairs(h3))
