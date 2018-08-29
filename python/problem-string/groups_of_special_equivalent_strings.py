#   https://leetcode.com/problems/groups-of-special-equivalent-strings

#   https://leetcode.com/problems/groups-of-special-equivalent-strings/solution


class Solution:
    #   74.49%
    def numSpecialEquivGroups(self, A):
        if A is None or 0 == len(A):
            return 0
        s = set()
        for a in A:
            if len(a) < 3:
                s.add(a)
                continue
            evens = sorted([c for i, c in enumerate(a) if 0 == i % 2])
            odds = sorted([c for i, c in enumerate(a) if 1 == i % 2])
            aa, evenIdx, oddIdx = [], 0, 0
            while evenIdx < len(evens) and oddIdx < len(odds):
                aa.append(evens[evenIdx])
                aa.append(odds[oddIdx])
                evenIdx += 1
                oddIdx += 1
            while evenIdx < len(evens):
                aa.append(evens[evenIdx])
                evenIdx += 1
            while oddIdx < len(odds):
                aa.append(odds[oddIdx])
                oddIdx += 1
            s.add(''.join(aa))
        return len(s)


s = Solution()
data = [(['a', 'b', 'c', 'a', 'c', 'c'], 3),
        (['aa', 'bb', 'ab', 'ba'], 4),
        (['abc', 'acb', 'bac', 'bca', 'cab', 'cba'], 3),
        (['abcd', 'cdab', 'adcb', 'cbad'], 1),
        ]
for A, expected in data:
    real = s.numSpecialEquivGroups(A)
    print('{}, expected {}, real {}, result {}'.format(A, expected, real, expected == real))
