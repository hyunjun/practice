#   https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree
#   82.04%


from ListNode import ListNode
from TreeNode import TreeNode


class Solution:
    def sortedListToBST(self, head):
        if head is None:
            return None
        nums = []
        while head:
            nums.append(head.val)
            head = head.next
        return self.sortedArrayToBSTRecur(nums)

    def sortedArrayToBSTRecur(self, nums):
        if nums is None or 0 == len(nums):
            return None
        mid = len(nums) // 2
        node = TreeNode(nums[mid])
        node.left = self.sortedArrayToBSTRecur(nums[:mid])
        node.right = self.sortedArrayToBSTRecur(nums[mid + 1:])
        return node


head = ListNode(-10)
head.next = ListNode(-3)
head.next.next = ListNode(0)
head.next.next.next = ListNode(5)
head.next.next.next.next = ListNode(9)
'''
        _______0______
       /              \
    __-3__          ___9__
   /      \        /      \
 -10       x       5       x
'''
s = Solution()
root = s.sortedListToBST(head)
print(root)
