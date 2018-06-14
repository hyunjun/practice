#   https://leetcode.com/problems/delete-node-in-a-linked-list
#   46.04%


from ListNode import ListNode


class Solution:
    def deleteNode(self, node):
        if node is None or node.next is None:
            return
        node.val = node.next.val
        node.next = node.next.next


s = Solution()
h1 = ListNode(0)
h1.next = ListNode(1)
print(h1)
s.deleteNode(h1)
print(h1)
