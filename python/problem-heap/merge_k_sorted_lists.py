#   https://leetcode.com/problems/merge-k-sorted-lists

#   https://leetcode.com/problems/merge-k-sorted-lists/solution


from ListNode import ListNode
import heapq
import sys


class Solution:
    #   40.75%
    def mergeKLists(self, lists):
        if all([l is None for l in lists]):
            return None
        heap, lIdx, k, head, prev = [], 0, len(lists), None, None
        for i in range(k):
            if lists[i]:
                heapq.heappush(heap, lists[i].val)
                lists[i] = lists[i].next
        while not all([l is None for l in lists]):
            if head is None:
                head = ListNode(heapq.heappop(heap))
                prev = head
            else:
                node = ListNode(heapq.heappop(heap))
                prev.next = node
                prev = node
            minVal = sys.maxsize
            for i in range(k):
                if lists[i] and lists[i].val < minVal:
                    minVal = lists[i].val
                    lIdx = i
            heapq.heappush(heap, lists[lIdx].val)
            lists[lIdx] = lists[lIdx].next
        while heap:
            if head is None:
                head = ListNode(heapq.heappop(heap))
                prev = head
            else:
                node = ListNode(heapq.heappop(heap))
                prev.next = node
                prev = node
        return head


s = Solution()
l1 = ListNode(1)
l1.next = ListNode(4)
l1.next.next = ListNode(5)
print(l1)
l2 = ListNode(1)
l2.next = ListNode(3)
l2.next.next = ListNode(4)
print(l2)
l3 = ListNode(2)
l3.next = ListNode(6)
print(l3)
l = s.mergeKLists([l1, l2, l3])
print(l)
print(s.mergeKLists([None]))
print(s.mergeKLists([None, ListNode(1)]))
print(s.mergeKLists([ListNode(1), ListNode(0)]))
