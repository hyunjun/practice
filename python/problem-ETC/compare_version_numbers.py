#   https://leetcode.com/problems/compare-version-numbers


class Solution:
    #   https://leetcode.com/explore/challenge/card/september-leetcoding-challenge/555/week-2-september-8th-september-14th/3454
    #   runtime; 24ms, 94.61%
    #   memory; 13.8MB, 56.81%
    def compareVersion(self, version1: str, version2: str) -> int:
        def convert(s):
            return int(s) if 0 < len(s) else 0

        v1, v2 = version1.split('.'), version2.split('.')
        for i in range(min(len(v1), len(v2))):
            n1, n2 = convert(v1[i]), convert(v2[i])
            if n1 == n2:
                continue
            if n1 < n2:
                return -1
            if n1 > n2:
                return 1
        for j in range(i + 1, len(v1)):
            if 0 < convert(v1[j]):
                return 1
        for j in range(i + 1, len(v2)):
            if 0 < convert(v2[j]):
                return -1
        return 0


s = Solution()
data = [("0.1", "1.1", -1),
        ("1.0.1", "1", 1),
        ("7.5.2.4", "7.5.3", -1),
        ("1.01", "1.001", 0),
        ("1.0", "1.0.0", 0),
        ("1.0", "1", 0),
        ]
for version1, version2, expect in data:
    real = s.compareVersion(version1, version2)
    print(f'{version1} {version2} expect {expect} real {real} result {expect == real}')
