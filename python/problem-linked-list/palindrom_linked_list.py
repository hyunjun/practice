# https://leetcode.com/problems/palindrome-linked-list
# 80.95%


from ListNode import ListNode


class Solution(object):
  def isPalindrome(self, head):
    """
    :type head: ListNode
    :rtype: bool
    """
    if head is None:
      return True

    data, cur = [], head
    while cur is not None:
      data.append(cur.val)
      cur = cur.next
    return data == data[::-1]


# not working e.g. [1, 3, 2, 4, 3, 2, 1]
class Solution2(object):
  def isPalindrome(self, head):
    """
    :type head: ListNode
    :rtype: bool
    """
    if head is None:
      return True

    list_len, cur = 0, head
    while cur is not None:
      list_len += 1
      cur = cur.next

    mid = list_len // 2

    half_sum, cur_cnt, cur = 0, 0, head
    while cur is not None:
      if cur_cnt < mid:
        half_sum += cur.val
        print('plus\tcur cnt {}\thalf sum {}'.format(cur_cnt, half_sum))
      elif mid < cur_cnt:
        half_sum -= cur.val
        print('minus\tcur cnt {}\thalf sum {}'.format(cur_cnt, half_sum))
      else:
        if list_len % 2 == 0 and mid == cur_cnt:
          half_sum -= cur.val
          print('minus\tcur cnt {}\thalf sum {}'.format(cur_cnt, half_sum))
      cur_cnt += 1
      cur = cur.next
    return half_sum == 0


head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(2)
head.next.next.next.next = ListNode(1)


s = Solution()
print(s.isPalindrome(head))
s2 = Solution2()
print(s2.isPalindrome(head))
