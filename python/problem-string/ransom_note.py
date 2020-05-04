#   https://leetcode.com/problems/ransom-note

#   https://leetcode.com/problems/ransom-note/discuss/132701/Python-One-Line-(beats-over-98-of-solutions)


from collections import Counter


class Solution:
    #   runtime; 91ms, 74.65%
    def canConstruct0(self, ransomNote, magazine):
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

    #   https://leetcode.com/explore/featured/card/may-leetcoding-challenge/534/week-1-may-1st-may-7th/3318
    #   runtime; 48ms, 67.18%
    #   memory; 14.1MB
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if ransomNote is None or 0 == len(ransomNote):
            return True
        if magazine is None or 0 == len(magazine):
            return False
        mCounter = Counter(magazine)
        for c in ransomNote:
            if c not in mCounter or mCounter[c] <= 0:
                return False
            mCounter[c] -= 1
        return True


s = Solution()
data = [('a', 'b', False), ('aa', 'ab', False), ('aa', 'aab', True)]
for r, m, expected in data:
    real = s.canConstruct(r, m)
    print('{}, {}, expected {}, real {}, result {}'.format(r, m, expected, real, expected == real))
