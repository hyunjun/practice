#   https://leetcode.com/problems/license-key-formatting


class Solution:
    #   37.60%
    def licenseKeyFormatting(self, S, K):
        res, w = [], []
        for s in S.split('-')[::-1]:
            for c in s[::-1]:
                if K == len(w):
                    res.append(''.join(w[::-1]).upper())
                    w = []
                w.append(c)
        if 0 < len(w):
            res.append(''.join(w[::-1]).upper())
        return '-'.join(res[::-1])


s = Solution()
data = [('5F3Z-2e-9-w', 4, '5F3Z-2E9W'),
        ('2-5g-3-J', 2, '2-5G-3J'),
        ('2-4A0r7-4k', 4, '24A0-R74K'),
        ]
for S, K, expected in data:
    real = s.licenseKeyFormatting(S, K)
    print('{}, {}, expected {}, real {}, result {}'.format(S, K, expected, real, expected == real))
