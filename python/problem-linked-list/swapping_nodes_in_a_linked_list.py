#   https://leetcode.com/problems/swapping-nodes-in-a-linked-list


from ListNode import ListNode


class Solution:
    #   https://leetcode.com/explore/challenge/card/march-leetcoding-challenge-2021/589/week-2-march-8th-march-14th/3671
    #   runtime: 992ms, 99.08%
    #   memory: 49MB, 31.79%
    def swapNodes(self, head: ListNode, k: int) -> ListNode:
        node, nodes = head, []
        while node:
            nodes.append(node)
            node = node.next
        nodes[k - 1].val, nodes[len(nodes) - k].val = nodes[len(nodes) - k].val, nodes[k - 1].val
        return head


s = Solution()
head1 = ListNode(1)
head1.next = ListNode(2)
head1.next.next = ListNode(3)
head1.next.next.next = ListNode(4)
head1.next.next.next.next = ListNode(5)
print(head1)
print(s.swapNodes(head1, 2))
