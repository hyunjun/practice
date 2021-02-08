#   https://leetcode.com/problems/longest-common-prefix
#   97.87%

class Solution:
    def longestCommonPrefix(self, strs):
        if strs is None or len(strs) <= 0:
            return ''
        if 1 == len(strs):
            return strs[0]

        minLen = len(strs[0])
        for s in strs:
            if len(s) < minLen:
                minLen = len(s)

        flag, result = True, []
        for curIdx in range(minLen):
            for i, s in enumerate(strs):
                if 0 == i:
                    result.append(s[curIdx])
                else:
                    if result[curIdx] != s[curIdx]:
                        if 0 < len(result):
                            result.pop()
                        flag = False
                        break
            curIdx += 1
            if not flag:
                break

        return ''.join(result)


data = [(['c', 'c'], 'c'), (['aa', 'a'], 'a'), (['', ''], ''), (['a'], 'a'), (['flower', 'flow', 'flight'], 'fl'), (['dog', 'racecar', 'car'], '')]
s = Solution()
for strs, expected in data:
    real = s.longestCommonPrefix(strs)
    print('strs {}, expected {}, real {}, result {}'.format(strs, expected, real, expected == real))
