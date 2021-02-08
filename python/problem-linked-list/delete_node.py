#   https://leetcode.com/problems/delete-node-in-a-linked-list
#   46.04%


from ListNode import ListNode


class Solution:
    def deleteNode(self, node):
        if node is None or node.next is None:
            return
        node.val = node.next.val
        node.next = node.next.next

    #   https://leetcode.com/explore/featured/card/june-leetcoding-challenge/539/week-1-june-1st-june-7th/3348
    #   runtime; 44ms, 29.74%
    #   memory; 14.2MB
    def deleteNode(self, node):
        p = None
        while node.next:
            node.val = node.next.val
            p, node = node, node.next
        p.next = None


s = Solution()
h1 = ListNode(0)
h1.next = ListNode(1)
print(h1)
s.deleteNode(h1)
print(h1)
