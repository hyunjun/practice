#   https://leetcode.com/problems/merge-k-sorted-lists

#   https://leetcode.com/problems/merge-k-sorted-lists/solution


from ListNode import ListNode
import heapq
import sys


class Solution:
    #   40.75%
    def mergeKLists0(self, lists):
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

    #   https://leetcode.com/explore/challenge/card/january-leetcoding-challenge-2021/582/week-4-january-22nd-january-28th/3615
    #   runtime; 92ms, 94.08%
    #   memory; 17.6MB, 93.98%
    def mergeKLists(self, lists):
        if lists is None or 0 == len(lists):
            return None
        lists = [head for head in lists if head]
        if 0 == len(lists):
            return None
        vals, lastNode = [], None
        for head in lists:
            if lastNode:
                lastNode.next = head
            node = head
            while node:
                vals.append(node.val)
                if node.next is None:
                    lastNode = node
                node = node.next
        vals.sort()
        i, node = 0, lists[0]
        while node:
            node.val = vals[i]
            i += 1
            node = node.next
        return lists[0]


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
