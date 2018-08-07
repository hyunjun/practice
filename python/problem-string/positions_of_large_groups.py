#   https://leetcode.com/problems/positions-of-large-groups

#   https://leetcode.com/problems/positions-of-large-groups/solution


class Solution:
    #   5.32%
    def largeGroupPositions(self, S):
        s, cnt, res = 0, 1, []
        for i, c in enumerate(S):
            if 0 == i:
                continue
            if S[i - 1] == c:
                cnt += 1
            else:
                if 2 < cnt:
                    res.append([s, i - 1])
                s = i
                cnt = 1
        if 2 < cnt:
            res.append([s, len(S) - 1])
        return res


s = Solution()
data = [('abbxxxxzzy', [[3,6]]),
        ('abc', []),
        ('abcdddeeeeaabbbcd', [[3,5],[6,9],[12,14]]),
        ]
for S, expected in data:
    real = s.largeGroupPositions(S)
    print('{}, expected {}, real {}, result {}'.format(S, expected, real, expected == real))
