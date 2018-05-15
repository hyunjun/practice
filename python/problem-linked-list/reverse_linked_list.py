#   https://leetcode.com/problems/reverse-linked-list
#   68.56%

#   https://leetcode.com/problems/reverse-linked-list/solution


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


class Solution:
    def reverseList(self, head):
        stack, cur = [], head
        while cur:
            stack.append(cur)
            cur = cur.next
        head = None
        while stack:
            if head:
                cur.next = stack.pop()
                cur = cur.next
            else:
                head = stack.pop()
                cur = head
        if cur:
            cur.next = None
        return head


s = Solution()
h1 = ListNode(1)
h1.next = ListNode(2)
h1.next.next = ListNode(3)
h1.next.next.next = ListNode(4)
h1.next.next.next.next = ListNode(5)
print(h1)
node = s.reverseList(h1)
print(node)
node = s.reverseList(ListNode(10))
print(node)
node = s.reverseList(None)
print(node)
