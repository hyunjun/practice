#   https://leetcode.com/problems/first-unique-character-in-a-string
#   67.90%


class Solution:
    def firstUniqChar(self, s):
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


solution = Solution()
data = [('leetcode', 0), ('loveleetcode', 2)]
for s, expected in data:
    real = solution.firstUniqChar(s)
    print('{}, expected {}, real {}, result {}'.format(s, expected, real, expected == real))
