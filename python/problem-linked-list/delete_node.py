#   https://leetcode.com/problems/delete-node-in-a-linked-list
#   46.04%


class Solution:
    def deleteNode(self, node):
        if node is None or node.next is None:
            return
        node.val = node.next.val
        node.next = node.next.next


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


s = Solution()
h1 = ListNode(0)
h1.next = ListNode(1)
print(h1)
s.deleteNode(h1)
print(h1)
