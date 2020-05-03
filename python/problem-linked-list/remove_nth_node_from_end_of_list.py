#   https://leetcode.com/problems/remove-nth-node-from-end-of-list

#   https://leetcode.com/problems/remove-nth-node-from-end-of-list/solution


from ListNode import ListNode


class Solution:
    #   runtime; 40ms, 99.95%
    def removeNthFromEnd0(self, head, n):
        if head is None:
            return None
        cur, nodes = head, []
        while cur:
            nodes.append(cur)
            cur = cur.next
        totalLen = len(nodes)
        print('total length {}'.format(totalLen))
        if n == totalLen:
            if 1 == totalLen:
                return None
            else:
                return nodes[1]
        if 1 == n:
            nodes[totalLen - (n + 1)].next = None
        else:
            print(nodes[totalLen - (n + 1)].val)
            print(nodes[totalLen - (n - 1)].val)
            nodes[totalLen - (n + 1)].next = nodes[totalLen - (n - 1)]
        return head

    #   runtime; 40ms, 99.95%
    def removeNthFromEnd1(self, head, n):
        if head is None:
            return None
        cur, cnt = head, 0
        while cur:
            cnt += 1
            cur = cur.next
        if cnt == n:
            return head.next
        cur = head
        while n + 1 < cnt:
            cnt -= 1
            cur = cur.next
        if cur.next:
            cur.next = cur.next.next
        return head

    #   runtime; 24ms, 96.97%
    #   memory; 13.9MB, 6.06%
    def removeNthFromEnd(self, head, n):
        stack, node = [], head
        while node:
            stack.append(node)
            node = node.next
        if 0 == len(stack):
            return head
        tIdx = len(stack) - n
        if tIdx < 0:
            return None
        if tIdx == 0:
            if 0 < len(stack[1:]):
                return stack[1]
            return None
        if 0 < tIdx < len(stack) - 1:
            stack[tIdx - 1].next = stack[tIdx + 1]
        if tIdx == len(stack) - 1:
            stack[tIdx - 1].next = None
        return stack[0]


s = Solution()
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
print(head)
print(s.removeNthFromEnd(head, 2))
#print(s.removeNthFromEnd(head, 1))
#print(s.removeNthFromEnd(head, 5))
print(s.removeNthFromEnd(ListNode(1), 1))
