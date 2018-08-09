#   https://leetcode.com/problems/remove-nth-node-from-end-of-list

#   https://leetcode.com/problems/remove-nth-node-from-end-of-list/solution


from ListNode import ListNode


class Solution:
    #   99.95%
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

    #   99.95%
    def removeNthFromEnd(self, head, n):
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
