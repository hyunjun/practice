#   https://leetcode.com/problems/jump-game-iii


from typing import List


class Solution:
    #   runtime; 240ms, 77.95%
    #   memory; 19.5MB, 100.00%
    def canReach(self, arr: List[int], start: int) -> bool:
        if arr is None or not (1 <= len(arr) <= 5 * 10 ** 4) or not (0 <= start < len(arr)):
            return False

        self.res, self.visited = False, set()
        def visit(idx):
            if arr[idx] == 0:
                self.res = True
                return
            if self.res or idx in self.visited:
                return
            self.visited.add(idx)
            if idx + arr[idx] < len(arr):
                visit(idx + arr[idx])
            if 0 <= idx - arr[idx]:
                visit(idx - arr[idx])
        visit(start)
        return self.res


s = Solution()
data = [([4, 2, 3, 0, 3, 1, 2], 5, True),
        ([4, 2, 3, 0, 3, 1, 2], 0, True),
        ([3, 0, 2, 1, 2], 2, False),
        ]
for arr, start, expected in data:
    real = s.canReach(arr, start)
    print(f'{arr} {start} expected {expected} real {real} result {expected == real}')
