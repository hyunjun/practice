#   https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree
#   82.04%


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __str__(self):
        lVal, rVal = 'x', 'x'
        if self.left is None and self.right is None:
            lVal, rVal = '', ''
        if self.left:
            lVal = self.left
        if self.right:
            rVal = self.right
        return '({} {} {})'.format(lVal, self.val, rVal)


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
