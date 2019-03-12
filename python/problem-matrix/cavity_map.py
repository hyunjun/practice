#   https://www.hackerrank.com/challenges/cavity-map


def cavityMap(grid):
    if grid is None or 0 == len(grid) or 0 == len(grid[0]):
        return grid
    ROW, COL = len(grid), len(grid[0])
    grid = [list(line) for line in grid]
    for i in [str(n) for n in range(9, 0, -1)]:
        for r in range(1, ROW - 1):
            for c in range(1, COL - 1):
                if i == grid[r][c]:
                    if grid[r - 1][c] < i and grid[r + 1][c] < i and grid[r][c - 1] < i and grid[r][c + 1] < i:
                        grid[r][c] = 'X'
    return [''.join(line) for line in grid]


data = [(['989', '191', '111'], ['989', '1X1', '111']),
        (['1112', '1912', '1892', '1234'], ['1112', '1X12', '18X2', '1234']),
        ]
for grid, expected in data:
    real = cavityMap(grid)
    print('{}, expected {}, real {}, result {}'.format(grid, expected, real, expected == real))
