# https://leetcode.com/problems/count-and-say/

class Solution(object):
  cache = {1: '1'}
  def countAndSay(self, n):
    """
    :type n: int
    :rtype: str
    """
    if n <= 0:
      return ''
    if n == 1:
      return '1'
    s = None
    if n - 1 in Solution.cache:
      s = Solution.cache[n - 1]
    else:
      s = self.countAndSay(n - 1)
    print('s {}'.format(s))
    s_idx, result = 0, []
    for i, c in enumerate(s):
      if 0 == i:
        continue
      if s[i - 1] != c:
        cnt = i - s_idx
        result.append('{}{}'.format(cnt, s[i - 1]))
        s_idx = i
    print('{}{}'.format(len(s) - s_idx, s[-1]))
    result.append('{}{}'.format(len(s) - s_idx, s[-1]))
    result_str = ''.join(result)
    Solution.cache[n] = result_str
    return Solution.cache[n]

s = Solution()
for i in range(7):
  print('{}\t{}'.format(i, s.countAndSay(i)))
