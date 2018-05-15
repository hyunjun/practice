#   https://leetcode.com/problems/remove-linked-list-elements
#   18.37%


class ListNode(object):
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


class Solution(object):
    def removeElements(self, head, val):
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
