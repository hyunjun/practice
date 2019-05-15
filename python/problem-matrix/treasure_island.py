#   https://aonecode.com/amazon-online-assessment-questions Q2


def min_path(grid):
    if grid is None or 0 == len(grid) or 0 == len(grid[0]):
        return []

    R, C = len(grid), len(grid[0])
    def isValid(r, c):
        if r < 0 or c < 0 or R <= r or C <= c:
            return False
        return True

    def recur(visited, path, r, c):
        if grid[r][c] == 'D' or (r, c) in visited:
            return []
        visited.add((r, c))
        path.append((r, c))
        if grid[r][c] == 'X':
            return path
        min_len, min_len_path = float('inf'), []
        for nr, nc in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
            if not isValid(nr, nc) or (nr, nc) in visited:
                continue
            cur_path = recur(visited, path[:], nr, nc)
            if 0 < len(cur_path) and len(cur_path) < min_len:
                min_len_path = cur_path
        return min_len_path

    return recur(set(), [], 0, 0)


grid = [['O', 'O', 'O', 'O'],
        ['D', 'O', 'D', 'O'],
        ['O', 'O', 'O', 'O'],
        ['X', 'D', 'D', 'O'],
        ]
print(min_path(grid))
