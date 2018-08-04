#   https://leetcode.com/problems/middle-of-the-linked-list

#   https://leetcode.com/problems/middle-of-the-linked-list/solution


from ListNode import ListNode


class Solution:
    #   20.89%
    def middleNode(self, head):
        if head is None:
            return None
        l, cur = [], head
        while cur:
            l.append(cur)
            cur = cur.next
        return l[len(l) // 2]


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
