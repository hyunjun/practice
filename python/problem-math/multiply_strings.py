#   https://leetcode.com/problems/multiply-strings
#   70.13%

class Solution(object):
  def multiply(self, num1, num2):
    """
    :type num1: str
    :type num2: str
    :rtype: str
    """
    if num1 is None or 0 == len(num1) or num2 is None or 0 == len(num2) or num1 == '0' or num2 == '0':
        return '0'
    s, nums = 0, {}
    for i, n in enumerate(num1[::-1]):
      for j, m in enumerate(num2[::-1]):
        n, m = int(n), int(m)
        if 0 == n or m == 0:
          continue
        if i + j in nums:
          nums[i + j] += n * m
        else:
          nums[i + j] = n * m
        #print('{}\t[{}] {} {}\t[{}] {} {}'.format(cur, i, n, tens[i], j, m, tens[j]))
    sup = 1
    #print(nums)
    for i in range(max(nums.keys()) + 1):
      if i in nums:
        #print(nums[i], sup)
        s += nums[i] * sup
      sup *= 10
    return str(s)

s = Solution()
cases = [('0', '0', '0'), ('47', '23', '1081'), ('123', '456', '56088'), ('123456789', '987654321', '121932631112635269'), ('93553535314', '25247452591474', '2361988447605003674312836'), ('401716832807512840963', '167141802233061013023557397451289113296441069', '67143675422804947379429215144664313370120390398055713625298709447')]
for num1, num2, expected in cases:
  real = s.multiply(num1, num2)
  print('{} * {} = {}\texpected {}\tresult {}'.format(num1, num2, real, expected, expected == real))
#print(s.multiply('47', '23'))   #   1081
#print(s.multiply('123', '456'))   #   56088
#print(s.multiply("123456789", "987654321")) #   121932631112635269
#print(s.multiply("93553535314", "25247452591474"))  # 2361988447605003674312836
#print(s.multiply("401716832807512840963", "167141802233061013023557397451289113296441069"))    # 67143675422804947379429215144664313370120390398055713625298709447
