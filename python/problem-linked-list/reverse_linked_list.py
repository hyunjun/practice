#   https://leetcode.com/problems/reverse-linked-list

#   https://leetcode.com/problems/reverse-linked-list/solution


from ListNode import ListNode


class Solution:
    #   68.56%
    def reverseList0(self, head):
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

    #   runtime; 28ms, 99.98%
    #   memory; 14.5MB, 45.42%
    def reverseList1(self, head):
        stack, cur = [], head
        while cur:
            stack.append(cur.val)
            cur = cur.next
        cur = head
        while stack:
            cur.val = stack.pop()
            cur = cur.next
        return head

    #   runtime; 56ms, 17.87%
    #   memory; 20.4MB, 5.05%
    def reverseList(self, head):
        if head is None:
            return head
        def reverse(node):
            if node.next is None:
                return node, node
            h, prev = reverse(node.next)
            prev.next = node
            return h, node
        newHead, last = reverse(head)
        last.next = None
        return newHead


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
