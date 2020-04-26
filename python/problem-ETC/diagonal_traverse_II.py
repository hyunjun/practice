#   https://leetcode.com/problems/diagonal-traverse-ii

#   https://leetcode.com/problems/diagonal-traverse-ii/discuss/597706/Python-No-fancy-code-short-solution-with-comments.


from typing import List


class Solution:
    #   runtime; 1488ms, 16.67%
    #   memory; 40.6MB, 100.00%
    #   (0, 0)을 tree root로 간주하고 bfs traverse
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        if nums is None or not (1 <= len(nums) <= 10 ** 5):
            return []
        R, C = len(nums), 0
        for r in range(R):
            C = max(C, len(nums[r]))
        q, ret, visited = [(0, 0)], [], set()
        while q:
            r, c = q.pop(0)
            if (r, c) in visited:
                continue
            visited.add((r, c))
            ret.append(nums[r][c])
            if r + 1 < R and c < len(nums[r + 1]):
                q.append((r + 1, c))
            if c + 1 < C and c + 1 < len(nums[r]):
                q.append((r, c + 1))
        return ret


s = Solution()
data = [([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [1, 4, 2, 7, 5, 3, 8, 6, 9]),
        ([[1, 2, 3, 4, 5], [6, 7], [8], [9, 10, 11], [12, 13, 14, 15, 16]], [1, 6, 2, 8, 7, 3, 9, 4, 12, 10, 5, 13, 11, 14, 15, 16]),
        ([[1, 2, 3], [4], [5, 6, 7], [8], [9, 10, 11]], [1, 4, 2, 5, 3, 8, 6, 9, 7, 10, 11]),
        ([[1, 2, 3, 4, 5, 6]], [1, 2, 3, 4, 5, 6]),
        ]
for nums, expected in data:
    real = s.findDiagonalOrder(nums)
    print(f'expected {expected} real {real} result {expected == real}')
