#   https://leetcode.com/problems/buddy-strings

#   https://leetcode.com/problems/buddy-strings/solution


from collections import Counter


class Solution:
    #   runtime; 60ms, 5.15%
    def buddyStrings0(self, A, B):
        if (A is None or 0 == len(A)) and (B is None or 0 == len(B)) or len(A) != len(B):
            return False

        def indices(s):
            d = {}
            for i, c in enumerate(s):
                if c in d:
                    d[c].add(i)
                else:
                    d[c] = set([i])
            return d

        dA, dB = indices(A), indices(B)
        if set(dA.keys()) != set(dB.keys()):
            return False

        cnt = 0
        for c, idxSet in dA.items():
            bIdxSet = dB[c]
            if len(idxSet) != len(bIdxSet):
                return False
            cnt += len(idxSet - bIdxSet)
        if 2 == cnt:
            return True

        for c, idxSet in dA.items():
            bIdxSet = dB[c]
            if idxSet == bIdxSet and 2 <= len(idxSet) and 2 <= len(bIdxSet):
                return True

        return False

    #   https://leetcode.com/explore/challenge/card/october-leetcoding-challenge/560/week-2-october-8th-october-14th/3492
    #   runtime; 32ms, 75.76%
    #   memory; 14.1MB
    def buddyStrings1(self, A: str, B: str) -> bool:
        if A is None or B is None or len(A) < 2 or len(B) < 2 or len(A) != len(B):
            return False
        diffs = []
        for i, c in enumerate(A):
            if c != B[i]:
                diffs.append(i)
        return (len(diffs) == 0 and any(cnt >= 2 for cnt in Counter(A).values())) or (len(diffs) == 2 and A[diffs[0]] == B[diffs[1]] and A[diffs[1]] == B[diffs[0]])

    #   runtime; 28ms, 91.67%
    #   memory; 14.2MB, 100.00%
    def buddyStrings(self, A: str, B: str) -> bool:
        if A is None or B is None or len(A) < 2 or len(B) < 2 or len(A) != len(B):
            return False
        diffs = [i for i, c in enumerate(A) if c != B[i]]
        return (len(diffs) == 0 and any(cnt >= 2 for cnt in Counter(A).values())) or (len(diffs) == 2 and A[diffs[0]] == B[diffs[1]] and A[diffs[1]] == B[diffs[0]])


s = Solution()
data = [('ab', 'ba', True),
        ('ab', 'ab', False),
        ('ab', 'ac', False),
        ('aa', 'aa', True),
        ('aaaaaaabc', 'aaaaaaacb', True),
        ('', 'aa', False),
        ('aaaaaaabbcc', 'aaaaaaabcbc', True),
        ]
for A, B, expected in data:
    real = s.buddyStrings(A, B)
    print('{}, {}, expected {}, real {}, result {}'.format(A, B, expected, real, expected == real))
