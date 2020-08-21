#   https://leetcode.com/problems/reorder-list


from ListNode import ListNode


class Solution:
    #   https://leetcode.com/explore/featured/card/august-leetcoding-challenge/551/week-3-august-15th-august-21st/3430
    #   runtime; 200ms, 5.12%
    #   memory; 23.2MB, 49.55%
    def reorderList0(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        n, nodes = head, []
        while n:
            nodes.append(n.val)
            n = n.next
        n = head
        while n:
            n.val = nodes.pop(0)
            n = n.next
            if n:
                n.val = nodes.pop()
                n = n.next

    #   runtime; 192ms, 5.68%
    #   memory; 23.2MB, 38.62%
    def reorderList(self, head: ListNode) -> None:
        n, cnt = head, 0
        while n:
            cnt += 1
            n = n.next
        n, i, nums, isHalfFilled = head, 0, [None] * cnt, False
        while n:
            nums[i] = n.val
            if isHalfFilled:
                i -= 2
            else:
                i += 2
                if i == len(nums):
                    i = len(nums) - 1
                    isHalfFilled = True
                elif i == len(nums) + 1:
                    i = len(nums) - 2
                    isHalfFilled = True
            n = n.next
        n, i = head, 0
        while n:
            n.val = nums[i]
            n = n.next
            i += 1


s = Solution()
h1 = ListNode(1)
h1.next = ListNode(2)
h1.next.next = ListNode(3)
h1.next.next.next = ListNode(4)
h2 = ListNode(1)
h2.next = ListNode(2)
h2.next.next = ListNode(3)
h2.next.next.next = ListNode(4)
h2.next.next.next.next = ListNode(5)
s.reorderList(h1)
print(h1)
s.reorderList(h2)
print(h2)
