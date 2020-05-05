#   https://leetcode.com/problems/first-unique-character-in-a-string


from collections import defaultdict


class Solution:
    #   runtime; 104ms, 67.90%
    def firstUniqChar0(self, s):
        if s is None or 0 == len(s):
            return -1
        cnt, idx = {}, {}
        for i, c in enumerate(s):
            if c in cnt:
                cnt[c] += 1
            else:
                cnt[c] = 1
                idx[c] = i
        for c in s:
            if 1 == cnt[c]:
                return idx[c]
        return -1

    #   https://leetcode.com/explore/featured/card/may-leetcoding-challenge/534/week-1-may-1st-may-7th/3320
    #   runtime; 188ms, 19.98%
    #   memory; 14MB
    def firstUniqChar(self, s: str) -> int:
        if s is None or 0 == len(s):
            return -1
        d, q = defaultdict(int), []
        for i, c in enumerate(s):
            d[c] += 1
            if d[c] == 1:
                q.append((c, i))
            else:
                if 0 < len(q) and q[0][0] == c:
                    q.pop(0)
        while 0 < len(q) and d[q[0][0]] != 1:
            q.pop(0)
        if 0 == len(q):
            return -1
        return q[0][1]


solution = Solution()
data = [('leetcode', 0),
        ('loveleetcode', 2),
        ]
for s, expected in data:
    real = solution.firstUniqChar(s)
    print(f'{s}, expected {expected}, real {real}, result {expected == real}')
