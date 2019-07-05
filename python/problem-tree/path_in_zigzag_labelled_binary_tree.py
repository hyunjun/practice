#   https://leetcode.com/problems/path-in-zigzag-labelled-binary-tree


from typing import List


class Solution:
    #   runtime; 36ms, 55.43%
    #   memory; 13.1MB, 100.00%
    def pathInZigZagTree(self, label: int) -> List[int]:
        if label < 1:
            return []
        if label == 1:
            return [1]
        height = 1
        while height <= label:
            height *= 2
        height //= 4
        res = [label]
        while res[-1] // 2 > 1:
            val = res[-1] // 2
            idx = val - height
            val = height + abs(height - 1 - idx)
            res.append(val)
            height //= 2
        res.append(1)
        return res[::-1]


s = Solution()
data = [(1, [1]),
        (8, [1, 2, 7, 8]),
        (14, [1, 3, 4, 14]),
        (26, [1, 2, 6, 10, 26]),
        ]
for label, expected in data:
    real = s.pathInZigZagTree(label)
    print(f'{label}, expected {expected}, real {real}, result {expected == real}')
