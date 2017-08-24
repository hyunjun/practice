# https://leetcode.com/problems/valid-palindrome/
# 1.58% of python submissions


class Solution(object):
  def isPalindrome(self, s):
    """
    :type s: str
    :rtype: bool
    """
    cleaned = []
    for c in s.lower():
      if c in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']:
        cleaned.append(c)
    ss = ''.join(cleaned)
    return ss == ss[::-1]


s = Solution()
for cand, expected in [('', True), ('A man, a plan, a canal: Panama', True), ('race a car', False)]:
  real = s.isPalindrome(cand)
  print('{}\texpected {}\treal {}\tresult {}'.format(cand, expected, real, expected == real))
