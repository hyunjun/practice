#   https://leetcode.com/problems/add-two-numbers


from ListNode import ListNode


class Solution:
    def calcValAndCarry(self, val, carry):
        if 1 == carry:
            val += 1
            carry = 0
        if 10 <= val:
            val -= 10
            carry = 1
        return val, carry

    #   runtime; 81.07%
    def addTwoNumbers(self, l1, l2):
        if l1 is None:
            return l2
        if l2 is None:
            return l1

        n1, n2 = l1, l2
        h, p, c, carry = None, None, None, 0
        while n1 is not None and n2 is not None:
            curVal = n1.val + n2.val
            curVal, carry = self.calcValAndCarry(curVal, carry)
            c = ListNode(curVal)
            #print('cur val {}, carry {}, head {}, prev {}, cur {}'.format(curVal, carry, h, p, c))
            if p is None:
                p = c
                if h is None:
                    h = p
            else:
                p.next = c
                p = c
            n1 = n1.next
            n2 = n2.next

        while n1 is not None:
            curVal = n1.val
            curVal, carry = self.calcValAndCarry(curVal, carry)
            c = ListNode(curVal)
            #print('cur val {}, carry {}, head {}, prev {}, cur {}'.format(curVal, carry, h, p, c))
            p.next = c
            p = c
            n1 = n1.next

        while n2 is not None:
            curVal = n2.val
            curVal, carry = self.calcValAndCarry(curVal, carry)
            c = ListNode(curVal)
            #print('cur val {}, carry {}, head {}, prev {}, cur {}'.format(curVal, carry, h, p, c))
            p.next = c
            p = c
            n2 = n2.next

        if 1 == carry:
            c = ListNode(1)
            p.next = c

        return h

    #   https://leetcode.com/explore/challenge/card/january-leetcoding-challenge-2021/580/week-2-january-8th-january-14th/3601
    #   runtime; 72ms, 51.91%
    #   memory; 14.3MB, 39.71%
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        vals, carry = [], 0
        while l1 and l2:
            val = l1.val + l2.val + carry
            if 9 < val:
                carry, val = 1, val - 10
            else:
                carry = 0
            l1, l2 = l1.next, l2.next
            vals.append(val)
        while l1:
            val = l1.val + carry
            if 9 < val:
                carry, val = 1, val - 10
            else:
                carry = 0
            l1 = l1.next
            vals.append(val)
        while l2:
            val = l2.val + carry
            if 9 < val:
                carry, val = 1, val - 10
            else:
                carry = 0
            l2 = l2.next
            vals.append(val)
        if carry:
            vals.append(1)
        for i, val in enumerate(vals):
            vals[i] = ListNode(val)
            if 0 < i:
                vals[i - 1].next = vals[i]
        return vals[0]


s = Solution()

l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)
l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)
print(s.addTwoNumbers(l1, l2))  # 7 0 8

print(s.addTwoNumbers(ListNode(0), ListNode(0)))

l1 = ListNode(9)
l1.next = ListNode(9)
l1.next.next = ListNode(9)
l1.next.next.next = ListNode(9)
l1.next.next.next.next = ListNode(9)
l1.next.next.next.next.next = ListNode(9)
l1.next.next.next.next.next.next = ListNode(9)
l2 = ListNode(9)
l2.next = ListNode(9)
l2.next.next = ListNode(9)
l2.next.next.next = ListNode(9)
print(s.addTwoNumbers(l1, l2))  #  8 9 9 9 0 0 0 1
