#   https://leetcode.com/problems/replace-all-s-to-avoid-consecutive-repeating-characters


class Solution:
    #   runtime; 24ms, 98.03%
    #   memory; 13.9MB, 45.97%
    def modifyString(self, s: str) -> str:
        ls = list(s)
        for i, c in enumerate(ls):
            if c != '?':
                continue
            avoid = set() if i < 0 else set([ls[i - 1]])
            if i + 1 < len(s):
                avoid.add(ls[i + 1])
            for r in range(ord('a'), ord('z') + 1):
                ch = chr(r)
                if ch not in avoid:
                    ls[i] = ch
                    break
        return ''.join(ls)


solution = Solution()
data = [("?zs", "azs"),
        ("ubv?w", "ubvaw"),
        ("j?qg??b", "jaqgacb"),
        ("??yw?ipkj?", "abywaipkja"),
        ]
for s, expect in data:
    real = solution.modifyString(s)
    print(f'{s} expect {expect} real {real} result {expect == real}')
