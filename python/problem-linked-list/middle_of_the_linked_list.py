#   https://leetcode.com/problems/middle-of-the-linked-list

#   https://leetcode.com/problems/middle-of-the-linked-list/solution


from ListNode import ListNode


class Solution:
    #   20.89%
    def middleNode0(self, head):
        if head is None:
            return None
        l, cur = [], head
        while cur:
            l.append(cur)
            cur = cur.next
        return l[len(l) // 2]

    #   https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/529/week-2/3290
    #   runtime; 32ms, 18.70%
    #   memory; 14MB
    def middleNode1(self, head):
        if head is None:
            return None
        node, cnt = head, 0
        while node:
            cnt += 1
            node = node.next
        target = cnt // 2
        node, cnt = head, 0
        while cnt < target:
            cnt += 1
            node = node.next
        return node

    #   runtime; 40ms
    #   memory; 13.7MB
    def middleNode(self, head):
        if head is None:
            return None
        node1, node2 = head, head
        while node2.next and node2.next.next:
            node1 = node1.next
            node2 = node2.next.next
        if node2.next is None:
            return node1
        return node1.next


s = Solution()

ll1 = ListNode(1)
ll1.next = ListNode(2)
ll1.next.next = ListNode(3)
ll1.next.next.next = ListNode(4)
ll1.next.next.next.next = ListNode(5)
print(s.middleNode(ll1))

ll2 = ListNode(1)
ll2.next = ListNode(2)
ll2.next.next = ListNode(3)
ll2.next.next.next = ListNode(4)
ll2.next.next.next.next = ListNode(5)
ll2.next.next.next.next.next = ListNode(6)
print(s.middleNode(ll2))
