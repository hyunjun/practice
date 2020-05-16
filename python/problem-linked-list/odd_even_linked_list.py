#   https://leetcode.com/problems/odd-even-linked-list

#   https://leetcode.com/problems/odd-even-linked-list/solution


from ListNode import ListNode


class Solution:
    #   Runtime Error
    def oddEvenList0(self, head):
        if head is None or head.next is None:
            return head
        cur, totalLen = head.next, 0
        while cur:
            totalLen += 1
            cur = cur.next
        print('total length {}'.format(totalLen))

        def getNextIdx(idx):
            if 0 == idx % 2:
                return idx // 2
            return totalLen // 2 + idx // 2 + 1
        #for i in range(1, totalLen + 1):
        #    print('{} -> {}'.format(i, getNextIdx(i)))

        def getNextNode(start, startIdx, node, nodeIdx, nextIdx):
            if nodeIdx < nextIdx:
                cnt = nextIdx - nodeIdx
                while cnt:
                    cnt -= 1
                    node = node.next
                return node
            cnt = nextIdx - startIdx
            while cnt:
                cnt -= 1
                start = start.next
            return start

        start, startIdx = head.next, 1
        prevVal, cur, curIdx = start.val, start, startIdx
        loopCnt = totalLen
        if 1 == loopCnt % 2:
            loopCnt -= 1
        print('loop count {}'.format(loopCnt))
        while loopCnt:
            loopCnt -= 1
            nIdx = getNextIdx(curIdx)
            print('{} -> {}'.format(curIdx, nIdx))
            n = getNextNode(start, startIdx, cur, curIdx, nIdx)
            print('n.val {} should be changed into {}'.format(n.val, prevVal))
            tmp = n.val
            n.val = prevVal
            prevVal = tmp
            cur = n
            curIdx = nIdx
            if curIdx == startIdx:
                start = cur = getNextNode(start, startIdx, start, curIdx, curIdx + 2)
                curIdx += 2
                startIdx = curIdx
                if start:
                    prevVal = start.val
                else:
                    break
        return head

    #   0.0%
    def oddEvenList1(self, head):
        if head is None or head.next is None:
            return head
        cur, totalLen = head.next, 0
        while cur:
            totalLen += 1
            cur = cur.next
        print('total length {}'.format(totalLen))

        loopCnt = totalLen
        if 1 == loopCnt % 2:
            loopCnt -= 1
        loopCnt //= 2
        start = head.next
        print('loop count {}, start from {}'.format(loopCnt, start.val))
        while loopCnt:
            cur, subCnt = start, loopCnt
            while subCnt:
                #print('before cur {} cur.next {}'.format(cur.val, cur.next.val))
                cur.val, cur.next.val = cur.next.val, cur.val
                #print(' after cur {} cur.next {}'.format(cur.val, cur.next.val))
                subCnt -= 1
                cur = cur.next.next
            loopCnt -= 1
            start = start.next
        return head

    #   https://leetcode.com/explore/featured/card/may-leetcoding-challenge/536/week-3-may-15th-may-21st/3331
    #   runtime; 80ms, 5.14%
    #   memory; 15.7MB
    def oddEvenList2(self, head: ListNode) -> ListNode:
        if head is None or head.next is None or head.next.next is None:
            return head
        peven, even, odd, hn, cnt = None, head, head.next, head.next, 0
        while even and odd:
            if cnt % 2 == 0:
                peven = even
                even.next = odd.next
                even = odd.next
            else:
                odd.next = even.next
                odd = even.next
            cnt += 1
        if even:
            even.next = hn
        else:
            peven.next = hn
        return head

    #   runtime; 60ms, 9.62%
    #   memory; 15.8MB
    def oddEvenList(self, head: ListNode) -> ListNode:
        if head is None or head.next is None or head.next.next is None:
            return head
        p, c, n, hn, cnt = None, head, head.next, head.next, 0
        while c and n:
            p = c
            c.next = n.next
            c = n.next
            c, n = n, c
            cnt += 1
        if cnt % 2 == 0:
            c.next = hn
        else:
            p.next = hn
        return head


s = Solution()

#   1 2 3
#   1 3 2
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
print(head)
print(s.oddEvenList(head))

#   1 2 3 4
#   1 3 2 4
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
print(head)
print(s.oddEvenList(head))

#   1 2 3 4 5
#   1 3 5 2 4
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
print(head)
print(s.oddEvenList(head))

#   1 2 3 4 5 6
#   1 3 5 2 4 6
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
head.next.next.next.next.next = ListNode(6)
print(head)
print(s.oddEvenList(head))

#   1 2 3 4 5 6 7
#   1 3 5 7 2 4 6
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
head.next.next.next.next.next = ListNode(6)
head.next.next.next.next.next.next = ListNode(7)
print(head)
print(s.oddEvenList(head))

'''
1 2 3 4 5 6 7 8
  3 2 5 4 7 6   1 <-> 2, 3 <-> 4, 5 <-> 6
    5 2 7 4     2 <-> 3, 4 <-> 5
      7 2       3 <-> 4
'''
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
head.next.next.next.next.next = ListNode(6)
head.next.next.next.next.next.next = ListNode(7)
head.next.next.next.next.next.next.next = ListNode(8)
print(head)
print(s.oddEvenList(head))
