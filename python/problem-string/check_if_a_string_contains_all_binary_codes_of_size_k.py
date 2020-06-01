#   https://leetcode.com/problems/check-if-a-string-contains-all-binary-codes-of-size-k


class Solution:
    #   runtime; 276ms, 99.24%
    #   memory; 26.8MB, 100.00%
    def hasAllCodes(self, s: str, k: int) -> bool:
        kSet, totalCnt = set(), 2 ** k
        for i in range(k, len(s) + 1):
            kSet.add(s[i - k:i])
            if len(kSet) == totalCnt:
                return True
        return False


solution = Solution()
data = [("00110110", 2, True),
        ("00110", 2, True),
        ("0110", 1, True),
        ("0110", 2, False),
        ("0000000001011100", 4, False),
        ]
for s, k, expect in data:
    real = solution.hasAllCodes(s, k)
    print(f'{s} {k} expect {expect} real {real} result {expect == real}')
