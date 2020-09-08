#   https://leetcode.com/problems/detect-pattern-of-length-m-repeated-k-or-more-times


from typing import List


class Solution:
    #   runtime; 40ms, 70.68%
    #   memory; 14MB, 6.37%
    def containsPattern(self, arr: List[int], m: int, k: int) -> bool:
        patterns, totalStr = set(tuple(arr[i:i + m]) for i in range(len(arr) - m + 1)), ' '.join(str(a) for a in arr)
        for pattern in patterns:
            patternStr = ' '.join(str(p) for p in pattern)
            if ' '.join(patternStr for _ in range(k)) in totalStr:
                return True
        return False


s = Solution()
data = [([1,2,4,4,4,4], 1, 3, True),
        ([1,2,1,2,1,1,1,3], 2, 2, True),
        ([1,2,1,2,1,3], 2, 3, False),
        ([1,2,3,1,2], 2, 2, False),
        ([2,2,2,2], 2, 3, False),
        ]
for arr, m, k, expect in data:
    real = s.containsPattern(arr, m, k)
    print(f'{arr} {m} {k} expect {expect} real {real} result {expect == real}')
