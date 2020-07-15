#   https://leetcode.com/problems/path-crossing


class Solution:
    #   runtime; 32ms, 70.30%
    #   memory; 13.9MB, 100.00%
    def isPathCrossing(self, path: str) -> bool:
        point, visited = [0, 0], set()
        visited.add(tuple(point))
        for p in path:
            if p == 'N':
                point[1] += 1
            elif p == 'S':
                point[1] -= 1
            elif p == 'E':
                point[0] += 1
            else:
                point[0] -= 1
            if tuple(point) in visited:
                return True
            visited.add(tuple(point))
        return False


s = Solution()
data = [('NES', False),
        ('NESWW', True),
        ]
for path, expect in data:
    real = s.isPathCrossing(path)
    print(f'{path} expect {expect} real {real} result {expect == real}')
