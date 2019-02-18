# https://leetcode.com/problems/group-anagrams
# 36.43%

class Solution(object):
  def groupAnagrams(self, strs):
    """
    :type strs: List[str]
    :rtype: List[List[str]]
    """
    if strs is None or 0 == len(strs):
      return []
    result_dict, index_dict = {}, {}
    for i, s in enumerate(strs):
      key = ''.join(sorted(s))
      if key in result_dict:
        result_dict[key].append(s)
      else:
        result_dict[key] = [s]
        index_dict[key] = i
    result = []
    for key, i in sorted(index_dict.items(), key=lambda t: t[1]):
      result.append(sorted(result_dict[key]))
    return result

cases = [(["eat", "tea", "tan", "ate", "nat", "bat"], [["ate", "eat","tea"], ["nat","tan"], ["bat"]])]
s = Solution()
for strs, expected in cases:
  real = s.groupAnagrams(strs)
  print('{}\texpected {}\treal {}\tresult {}'.format(strs, expected, real, expected == real))
