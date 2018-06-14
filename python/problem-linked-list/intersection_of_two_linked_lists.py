#   https://leetcode.com/problems/intersection-of-two-linked-lists

#   https://leetcode.com/problems/intersection-of-two-linked-lists/solution


from ListNode import ListNode


class Solution:
    #   99.57%  time O(A + B), space O(A) or O(B)
    def getIntersectionNode0(self, headA, headB):
        if headA is None or headB is None:
            return None
        s = set()
        cur = headA
        while cur:
            s.add(cur)
            cur = cur.next
        cur = headB
        while cur:
            if cur in s:
                return cur
            cur = cur.next
        return None

    #   83.31%  time O(A + B), space O(1)
    def getIntersectionNode(self, headA, headB):
        if headA is None or headB is None:
            return None
        flagA, curA, flagB, curB = True, headA, True, headB
        while curA and curB:
            if curA is curB:
                return curA
            if curA.next is None and curB.next is None:
                return None
            curA = curA.next
            if curA is None:
                if flagA:
                    curA = headB
                else:
                    curA = headA
                flagA = not flagA
            curB = curB.next
            if curB is None:
                if flagB:
                    curB = headA
                else:
                    curB = headB
                flagB = not flagB
        return None


s = Solution()
'''
A:          a1 → a2
                   ↘
                     c1 → c2 → c3
                   ↗            
B:     b1 → b2 → b3
'''
h1 = ListNode('a1')
h1.next = ListNode('a2')
h1.next.next = ListNode('c1')
h1.next.next.next = ListNode('c2')
h1.next.next.next.next = ListNode('c3')
h2 = ListNode('b1')
h2.next = ListNode('b2')
h2.next.next = ListNode('b3')
h2.next.next.next = h1.next.next
print('c1' == s.getIntersectionNode(h1, h2).val)
