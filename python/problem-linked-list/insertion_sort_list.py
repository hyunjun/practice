#   https://leetcode.com/problems/insertion-sort-list

#   https://leetcode.com/problems/insertion-sort-list/solution


from ListNode import ListNode


class Solution:
    #   https://leetcode.com/explore/challenge/card/november-leetcoding-challenge/564/week-1-november-1st-november-7th/3517
    #   runtime; 4220ms
    #   memory; 15.9MB
    def insertionSortList(self, head: ListNode) -> ListNode:
        if head is None:
            return None
        n, nodes = head, []
        while n:
            nodes.append(n)
            for i in range(len(nodes) - 1, 0, -1):
                if nodes[i - 1].val <= nodes[i].val:
                    break
                nodes[i - 1].val, nodes[i].val = nodes[i].val, nodes[i - 1].val
            n = n.next
        return nodes[0]


s = Solution()
head1 = ListNode(4)
head1.next = ListNode(2)
head1.next.next = ListNode(1)
head1.next.next.next = ListNode(3)
head2 = ListNode(-1)
head2.next = ListNode(5)
head2.next.next = ListNode(3)
head2.next.next.next = ListNode(4)
head2.next.next.next.next = ListNode(0)
data = [head1, head2]
for head in data:
    print(head)
    print(s.insertionSortList(head))
