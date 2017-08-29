# https://leetcode.com/problems/letter-combinations-of-a-phone-number/
# 28.39%

'''
class Solution:
    # @return a list of strings, [s1, s2]
    def letterCombinations(self, digits):
        if '' == digits: return []
        kvmaps = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        return reduce(lambda acc, digit: [x + y for x in acc for y in kvmaps[digit]], digits, [''])
'''

from functools import reduce


class Solution(object):
  digitDict = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
  def letterCombinations(self, digits):
    """
    :type digits: str
    :rtype: List[str]
    """
    if digits is None or 0 == len(digits):
      return []
    digits = [digit for digit in digits if digit not in ['0', '1']]
    if 0 == len(digits):
      return []

    maxes = [len(Solution.digitDict[d]) for d in digits]
    totProduct = reduce(lambda a, b: a * b, maxes)
    changes = [totProduct // maxes[0]]
    for i in range(1, len(maxes)):
      changes.append(changes[i - 1] // maxes[i])
    indices = [0 for i in range(len(digits))]
    result = []

    for i in range(totProduct):
      s = []
      for j, c in enumerate(changes):
        if i != 0 and i % c == 0:
          indices[j] += 1
          if indices[j] >= maxes[j]:
            indices[j] = 0
        s.append(Solution.digitDict[digits[j]][indices[j]])
      result.append(''.join(s))
    return result

s = Solution()
print(s.letterCombinations('12'))
print(s.letterCombinations('2029'))
print(s.letterCombinations('9387'))
