#   https://leetcode.com/problems/add-two-numbers
#   81.07%


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        res = '({})->'.format(self.val)
        if self.next:
            res += str(self.next)
        else:
            res += 'None'
        return res


class Solution:
    def calcValAndCarry(self, val, carry):
        if 1 == carry:
            val += 1
            carry = 0
        if 10 <= val:
            val -= 10
            carry = 1
        return val, carry

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

l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)
print(l1)
l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(6)
l2.next.next.next = ListNode(6)
print(l2)

s = Solution()
r = s.addTwoNumbers(l1, l2)
print(r)
