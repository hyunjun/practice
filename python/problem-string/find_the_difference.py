#   https://leetcode.com/problems/find-the-difference

#   https://leetcode.com/problems/find-the-difference/discuss/133924/Python-Bitmap-(XOR)-solution
#   https://leetcode.com/problems/find-the-difference/discuss/86845/1-liners-and-2-liner-in-Python


from collections import Counter


class Solution:
    #   runtime; 24ms, 94.82%
    def findTheDifference0(self, s, t):
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

    #   https://leetcode.com/explore/challenge/card/september-leetcoding-challenge/557/week-4-september-22nd-september-28th/3471
    #   runtime; 44ms, 26.53%
    #   memory; 14MB, 19.65%
    def findTheDifference(self, s: str, t: str) -> str:
        return ''.join((Counter(t) - Counter(s)).keys())


solution = Solution()
data = [('', 'y', 'y'),
        ('a', 'aa', 'a'),
        ('abcd', 'abcde', 'e'),
        ]
for s, t, expect in data:
    real = solution.findTheDifference(s, t)
    print(f'{s}, {t}, expect {expect}, real {real}, result {expect == real}')
