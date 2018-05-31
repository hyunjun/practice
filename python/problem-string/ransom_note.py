#   https://leetcode.com/problems/ransom-note
#   74.65%

#   https://leetcode.com/problems/ransom-note/discuss/132701/Python-One-Line-(beats-over-98-of-solutions)


class Solution:
    def canConstruct(self, ransomNote, magazine):
        if ransomNote is None or 0 == len(ransomNote):
            return True
        if magazine is None or 0 == len(magazine):
            return False
        r = {}
        for c in ransomNote:
            if c in r:
                r[c] += 1
            else:
                r[c] = 1
        m = {}
        for c in magazine:
            if c in m:
                m[c] += 1
            else:
                m[c] = 1
        for c, cnt in r.items():
            if c in m:
                if m[c] < cnt:
                    return False
            else:
                return False
        return True


s = Solution()
data = [('a', 'b', False), ('aa', 'ab', False), ('aa', 'aab', True)]
for r, m, expected in data:
    real = s.canConstruct(r, m)
    print('{}, {}, expected {}, real {}, result {}'.format(r, m, expected, real, expected == real))
