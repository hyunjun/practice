#   https://leetcode.com/problems/shortest-distance-to-a-character

#   https://leetcode.com/problems/shortest-distance-to-a-character/solution


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


s = Solution()
data = [('loveleetcode', 'e', [3, 2, 1, 0, 1, 0, 0, 1, 2, 2, 1, 0]),
        ]
for S, C, expected in data:
    real = s.shortestToChar(S, C)
    print('{}, {}, expected {}, real {}, result {}'.format(S, C, expected, real, expected == real))
