#   https://leetcode.com/problems/shortest-distance-to-a-character

#   https://leetcode.com/problems/shortest-distance-to-a-character/solution


from typing import List


class Solution:
    #   78.70%
    def shortestToChar(self, S, C):
        cIdx, res = -1, []
        for i, c in enumerate(S):
            if C == c:
                res.append(0)
                cIdx = i
            else:
                if -1 == cIdx:
                    res.append(len(S))
                else:
                    res.append(abs(cIdx - i))
        for i in range(len(S) - 1, -1, -1):
            if C == S[i]:
                cIdx = i
            else:
                res[i] = min(res[i], abs(cIdx - i))
        return res

    #   https://leetcode.com/explore/challenge/card/february-leetcoding-challenge-2021/584/week-1-february-1st-february-7th/3631
    #   runtime; 40ms, 82.09%
    #   memory; 14.4MB, 61.15%
    def shortestToChar(self, s: str, c: str) -> List[int]:
        ret = [float('inf')] * len(s)
        for i, ch in enumerate(s):
            if ch == c:
                l, lDistance, r, rDistance = i - 1, 1, i + 1, 1
                ret[i] = 0
                while 0 <= l and s[l] != c:
                    ret[l] = min(ret[l], lDistance)
                    l -= 1
                    lDistance += 1
                while r <= len(s) - 1 and s[r] != c:
                    ret[r] = min(ret[r], rDistance)
                    r += 1
                    rDistance += 1
        return ret


s = Solution()
data = [('loveleetcode', 'e', [3, 2, 1, 0, 1, 0, 0, 1, 2, 2, 1, 0]),
        ('aaab', 'b', [3, 2, 1, 0]),
        ]
for S, C, expect in data:
    real = s.shortestToChar(S, C)
    print(f'{S}, {C}, expect {expect}, real {real}, result {expect == real}')
