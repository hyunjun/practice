#   https://leetcode.com/explore/featured/card/recursion-i/253/conclusion/2382


from ListNode import ListNode


class Solution:
    #   runtime; 40ms, 36.19%
    #   memory; 13.8MB
    def mergeTwoLists0(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is None and l2 is None:
            return None
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        nodes = []
        n1, n2 = l1, l2
        while n1 and n2:
            if n1.val == n2.val:
                nodes.append(ListNode(n1.val))
                nodes.append(ListNode(n1.val))
                n1 = n1.next
                n2 = n2.next
            elif n1.val > n2.val:
                nodes.append(ListNode(n2.val))
                n2 = n2.next
            else:
                nodes.append(ListNode(n1.val))
                n1 = n1.next
        while n1:
            nodes.append(ListNode(n1.val))
            n1 = n1.next
        while n2:
            nodes.append(ListNode(n2.val))
            n2 = n2.next
        for i in range(len(nodes) - 1):
            nodes[i].next = nodes[i + 1]
        return nodes[0]

    #   https://leetcode.com/explore/challenge/card/january-leetcoding-challenge-2021/579/week-1-january-1st-january-7th/3592
    #   runtime; 40ms, 36.19% -> 28ms, 98.10%
    #   memory; 14.1MB -> 14.3MB
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is None and l2 is None:
            return None
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        if l1.val < l2.val:
            h = l1
            l1 = l1.next
        else:
            h = l2
            l2 = l2.next
        n = h
        while l1 and l2:
            if l1.val < l2.val:
                n.next = l1
                l1 = l1.next
            else:
                n.next = l2
                l2 = l2.next
            n = n.next
        while l1:
            n.next = l1
            l1 = l1.next
            n = n.next
        while l2:
            n.next = l2
            l2 = l2.next
            n = n.next
        return h


s = Solution()
l1 = ListNode(1)
l1.next = ListNode(2)
l1.next.next = ListNode(4)
l2 = ListNode(1)
l2.next = ListNode(3)
l2.next.next = ListNode(4)
print(s.mergeTwoLists(l1, l2))
