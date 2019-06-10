#   https://leetcode.com/problems/height-checker


from typing import List


class Solution:
    #   runtime; 36ms, 59.56%
    #   memory; 13.3MB, 100.00%
    def heightChecker(self, heights: List[int]) -> int:
        if heights is None or 0 == len(heights):
            return 0
        cnt, sortedHeights = 0, sorted(heights)
        for i, h in enumerate(heights):
            if h != sortedHeights[i]:
                cnt += 1
        return cnt


s = Solution()
data = [([1, 1, 4, 2, 1, 3], 3),
        ([1, 5, 9, 3, 2, 2, 1, 8], 7),
        ]
for heights, expected in data:
    real = s.heightChecker(heights)
    print(f'{heights}, expected {expected}, real {real}, result {expected == real}')
