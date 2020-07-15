#   https://leetcode.com/problems/path-crossing


class Solution:
    #   runtime; 32ms, 70.30%
    #   memory; 13.9MB, 100.00%
    def isPathCrossing0(self, path: str) -> bool:
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

    #   runtime; 40ms, 40.97%
    #   memory; 13.9MB, 100.00%
    def isPathCrossing(self, path: str) -> bool:
        point, visited, d = [0, 0], set(), {'N': [0, 1], 'S': [0, -1], 'E': [1, 0], 'W': [-1, 0]}
        visited.add(tuple(point))
        for p in path:
            n = d[p]
            point[0] += n[0]
            point[1] += n[1]
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
