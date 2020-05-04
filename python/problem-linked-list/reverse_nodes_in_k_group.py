#   https://leetcode.com/problems/reverse-nodes-in-k-group


from ListNode import ListNode


class Solution:
    #   runtime; 52ms, 94.20%
    #   memory; 14MB, 81.45%
    def reverseKGroup0(self, head: ListNode, k: int) -> ListNode:
        if head is None:
            return head
        fst, snd, stack = head, head, []
        while fst and snd:
            cnt = 0
            while cnt < k and fst:
                stack.append(fst.val)
                fst = fst.next
                cnt += 1
            if k == len(stack):
                while stack:
                    snd.val = stack.pop()
                    snd = snd.next
        return head

    #   https://codebasil.com/problems/reverse-a-linked-list-in-groups
    #   runtime; 52ms, 51.88%
    #   memory; 14.8MB, 5.88%
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if head is None:
            return None
        n, nodes = head, []
        while n:
            nodes.append(n)
            n = n.next
        i = 0
        while i < len(nodes):
            l, r = i, i + k - 1
            if len(nodes) - 1 < r:
                break
            while l < r:
                nodes[l].val, nodes[r].val = nodes[r].val, nodes[l].val
                l += 1
                r -= 1
            i += k
        return nodes[0]

s = Solution()

head1 = ListNode(1)
head1.next = ListNode(2)
head1.next.next = ListNode(3)
head1.next.next.next = ListNode(4)
head1.next.next.next.next = ListNode(5)
print(head1)
print(s.reverseKGroup(head1, 2))

head2 = ListNode(1)
head2.next = ListNode(2)
head2.next.next = ListNode(3)
head2.next.next.next = ListNode(4)
head2.next.next.next.next = ListNode(5)
print(head2)
print(s.reverseKGroup(head2, 3))
