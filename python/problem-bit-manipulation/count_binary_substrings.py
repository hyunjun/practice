#   https://leetcode.com/problems/count-binary-substrings

#   https://leetcode.com/problems/count-binary-substrings/solution


class Solution:
    #   5.52%
    def countBinarySubstrings0(self, s):
        if s is None or 0 == len(s):
            return 0
        prev, d, count = '', {'0': 0, '1': 0}, 0
        for n in s:
            if prev != n:
                prev = n
                d[n] = 1
            else:
                d[n] += 1
            if 0 < d['0'] and 0 < d['1']:
                count += 1
            if '0' == n:
                d['1'] -= 1
            else:
                d['0'] -= 1
        return count

    #   https://leetcode.com/explore/featured/card/april-leetcoding-challenge-2021/596/week-4-april-22nd-april-28th/3718
    #   runtime; 376ms
    #   memory; 14.6MB, 43.11% 
    def countBinarySubstrings1(self, s: str) -> int:
        i, cnt = 0, 0
        while i < len(s):
            j = i + 1
            while j < len(s) and s[j] == s[i]:
                j += 1
            aCnt = j - i
            k = j
            while k < len(s) and s[k] != s[i]:
                k += 1
            bCnt = k - j
            cnt += min(aCnt, bCnt)
            i = j
        return cnt

    #   runtime; 228ms, 16.60%
    #   memory; 14.6MB, 74.01%
    def countBinarySubstrings(self, s: str) -> int:
        cnt, d = 0, {'0': 0, '1': 0}
        for i, n in enumerate(s):
            if 0 == i or s[i - 1] == n:
                d[n] += 1
            else:
                cnt += min(d.values())
                d[n] = 1
        return cnt + min(d.values())


solution = Solution()
data = [('00110011', 6),
        ('10101', 4),
        ('00110', 3),
        ('00100', 2),
        ('000', 0),
        ('111', 0),
        ]
for s, expected in data:
    real = solution.countBinarySubstrings(s)
    print('{}, expected {}, real {}, result {}'.format(s, expected, real, expected == real))
