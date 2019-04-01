#   https://leetcode.com/problems/next-greater-node-in-linked-list


from ListNode import ListNode


class Solution:
    #   Wrong Answer
    def nextLargerNodes0(self, head):
        if head.next is None:
            return [0]
        values, n = [], head
        while n:
            values.append(n.val)
            n = n.next
        res, nb, n2b = [0], values[-1], values[-1]
        for i in range(len(values) - 2, -1, -1):
            if values[i] >= nb:
                nb = n2b = values[i]
                res.append(0)
            else:
                if values[i] < n2b:
                    res.append(n2b)
                else:
                    res.append(nb)
                n2b = values[i]
        return res[::-1]

    #   runtime; 484ms, 17.18%
    #   memory; 17.6MB, 100.00%
    def nextLargerNodes(self, head):
        if head.next is None:
            return [0]
        values, n = [], head
        while n:
            values.append(n.val)
            n = n.next
        biggers, res = [], []
        while values:
            value = values.pop()
            i, biggerNum = len(biggers) - 1, 0
            while 0 <= i:
                if biggers[i] > value:
                    biggerNum = biggers[i]
                    break
                biggers.pop()
                i -= 1
            res.append(biggerNum)
            biggers.append(value)
        return res[::-1]


s = Solution()
head1 = ListNode(2)
head1.next = ListNode(1)
head1.next.next = ListNode(5)
head2 = ListNode(2)
head2.next = ListNode(7)
head2.next.next = ListNode(4)
head2.next.next.next = ListNode(3)
head2.next.next.next.next = ListNode(5)
head3 = ListNode(1)
head3.next = ListNode(7)
head3.next.next = ListNode(5)
head3.next.next.next = ListNode(1)
head3.next.next.next.next = ListNode(9)
head3.next.next.next.next.next = ListNode(2)
head3.next.next.next.next.next.next = ListNode(5)
head3.next.next.next.next.next.next.next = ListNode(1)
head4 = ListNode(3)
head4.next = ListNode(3)
head5 = ListNode(9)
head5.next = ListNode(7)
head5.next.next = ListNode(6)
head5.next.next.next = ListNode(7)
head5.next.next.next.next = ListNode(6)
head5.next.next.next.next.next = ListNode(9)
head6 = ListNode(4)
head6.next = ListNode(3)
head6.next.next = ListNode(2)
head6.next.next.next = ListNode(5)
head6.next.next.next.next = ListNode(1)
head6.next.next.next.next.next = ListNode(8)
head6.next.next.next.next.next.next = ListNode(10)
data = [(head1, [5, 5, 0]),
        (head2, [7, 0, 5, 5, 0]),
        (head3, [7, 9, 9, 9, 0, 5, 0, 0]),
        (head4, [0, 0]),
        (head5, [0, 9, 7, 9, 9, 0]),
        (head6, [5, 5, 5, 8, 8, 10, 0]),
        ]
for head, expected in data:
    real = s.nextLargerNodes(head)
    print('{}, expected {}, real {}, result {}'.format(head, expected, real, expected == real))
