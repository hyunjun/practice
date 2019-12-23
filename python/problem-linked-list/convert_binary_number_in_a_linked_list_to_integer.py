#   https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer


from ListNode import ListNode


class Solution:
    #   runtime; 28ms, 67.06%
    #   memory; 12.8MB, 100.00%
    def getDecimalValue0(self, head: ListNode) -> int:
        if head is None:
            return 0
        bins, node = [], head
        while node:
            bins.append(node.val)
            node = node.next
        maxLen = len(bins)
        return sum(b * 2 ** (maxLen - i - 1) for i, b in enumerate(bins))

    #   runtime; 28ms, 67.06%
    #   memory; 12.8MB, 100.00%
    def getDecimalValue1(self, head: ListNode) -> int:
        if head is None:
            return 0
        bins, node = [], head
        while node:
            bins.append(node.val)
            node = node.next
        return int(''.join(str(b) for b in bins), 2)

    #   runtime; 32ms, 26.98%
    #   memory; 12.8MB, 100.00%
    def getDecimalValue(self, head: ListNode) -> int:
        if head is None:
            return 0
        bins, node = [], head
        while node:
            bins.append(str(node.val))
            node = node.next
        return int(''.join(bins), 2)


s = Solution()
head1 = ListNode(1)
head1.next = ListNode(0)
head1.next.next = ListNode(1)
head2 = ListNode(0)
head3 = ListNode(1)
head4 = ListNode(1)
head4.next = ListNode(0)
head4.next.next = ListNode(0)
head4.next.next.next = ListNode(1)
head4.next.next.next.next = ListNode(0)
head4.next.next.next.next.next = ListNode(0)
head4.next.next.next.next.next.next = ListNode(1)
head4.next.next.next.next.next.next.next = ListNode(1)
head4.next.next.next.next.next.next.next.next = ListNode(1)
head4.next.next.next.next.next.next.next.next.next = ListNode(0)
head4.next.next.next.next.next.next.next.next.next.next = ListNode(0)
head4.next.next.next.next.next.next.next.next.next.next.next = ListNode(0)
head4.next.next.next.next.next.next.next.next.next.next.next.next = ListNode(0)
head4.next.next.next.next.next.next.next.next.next.next.next.next.next = ListNode(0)
head4.next.next.next.next.next.next.next.next.next.next.next.next.next.next = ListNode(0)
data = [(head1, 5),
        (head2, 0),
        (head3, 1),
        (head4, 18880),
        ]
for head, expected in data:
    real = s.getDecimalValue(head)
    print(f'{head} expected {expected} real {real} result {expected == real}')
