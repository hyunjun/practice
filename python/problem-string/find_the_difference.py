#   https://leetcode.com/problems/find-the-difference
#   94.82%

#   https://leetcode.com/problems/find-the-difference/discuss/133924/Python-Bitmap-(XOR)-solution
#   https://leetcode.com/problems/find-the-difference/discuss/86845/1-liners-and-2-liner-in-Python


class Solution:

    def findTheDifference(self, s, t):
        sDict, tDict = {}, {}
        for c in s:
            if c in sDict:
                sDict[c] += 1
            else:
                sDict[c] = 1
        for c in t:
            if c in tDict:
                tDict[c] += 1
            else:
                tDict[c] = 1
        for c, cnt in tDict.items():
            if c not in sDict or 1 == cnt - sDict[c]:
                return c
        return None


solution = Solution()
data = [('', 'y', 'y'), ('a', 'aa', 'a'), ('abcd', 'abcde', 'e')]
for s, t, expected in data:
    real = solution.findTheDifference(s, t)
    print('{}, {}, expected {}, real {}, result {}'.format(s, t, expected, real, expected == real))
