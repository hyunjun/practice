#   https://www.hackerrank.com/challenges/grid-challenge


#   Wrong Answer for 11/13
def gridChallenge0(grid):
    for i, g in enumerate(grid):
        g = sorted(g)
        if 0 == i:
            continue
        for j, c in enumerate(g):
            if grid[i - 1][j] > c:
                return 'NO'
    return 'YES'


def gridChallenge(grid):
    sorted_grid = []
    for g in grid:
        sorted_grid.append(sorted(g))

    for i, g in enumerate(sorted_grid):
        if 0 == i:
            continue
        for j, c in enumerate(g):
            if sorted_grid[i - 1][j] > c:
                return 'NO'
    return 'YES'


data = [(['abc', 'ade', 'efg'], 'YES'),
        (['ebacd', 'fghij', 'olmkn', 'trpqs', 'xywuv'], 'YES'),
        (['iv', 'sm'], 'NO'),
        (['abc', 'hjk', 'mpq', 'rtv'], 'YES'),
        (['mpxz', 'abcd' 'wlmf'], 'NO'),
        ]
for grid, expected in data:
    real = gridChallenge(grid)
    for g in grid:
        print(g)
    print('expected {}, real {}, result {}'.format(expected, real, expected == real))
