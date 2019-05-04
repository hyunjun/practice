#   https://medium.freecodecamp.org/bet-you-cant-solve-this-google-interview-question-4a6e5a4dc8ee


from collections import defaultdict


def number_of_largest_contiguous_block(grid):
    if grid is None or 0 == len(grid) or 0 == len(grid[0]):
        return 0

    R, C = len(grid), len(grid[0])
    parent = [r * C + c for r in range(R) for c in range(C)]

    def getParent(r, c):
        p = parent[r * C + c]
        while p != parent[p]:
            p = parent[p]
        return p

    def union(r0, c0, r1, c1):
        p0, p1 = getParent(r0, c0), getParent(r1, c1)
        if p0 < p1:
            parent[p1] = p0
        else:
            parent[p0] = p1

    for r in range(1, R):
        if grid[r][0] == grid[r - 1][0]:
            union(r, 0, r - 1, 0)
    for c in range(1, C):
        if grid[0][c] == grid[0][c - 1]:
            union(0, c, 0, c - 1)
    for r in range(1, R):
        for c in range(1, C):
            if grid[r][c] == grid[r - 1][c] == grid[r][c - 1]:
                union(r, c, r, c - 1)
                union(r, c, r - 1, c)
            elif grid[r][c] == grid[r][c - 1]:
                union(r, c, r, c - 1)
            elif grid[r][c] == grid[r - 1][c]:
                union(r, c, r - 1, c)
    d = defaultdict(int)
    #for r in range(R):
    #    print(['{:03d}'.format(parent[r * C + c]) for c in range(C)])
    for r in range(R):
        for c in range(C):
            d[getParent(r, c)] += 1
    return max(d.values())


data = [([[1, 1, 2, 3], [1, 2, 3, 2], [3, 2, 2, 2]], 5),
        ([[1, 1, 2, 1, 1, 3, 3, 1, 3, 1], [1, 3, 3, 3, 2, 3, 3, 3, 2, 1], [2, 2, 2, 2, 3, 2, 3, 2, 2, 2], [2, 2, 2, 1, 2, 1, 1, 1, 3, 2], [1, 1, 1, 3, 2, 3, 1, 3, 2, 3], [3, 1, 1, 3, 3, 1, 1, 3, 2, 3], [3, 2, 1, 3, 1, 3, 2, 1, 1, 1], [1, 2, 3, 3, 3, 3, 1, 1, 3, 3], [3, 3, 2, 1, 2, 2, 1, 3, 3, 2], [3, 1, 1, 1, 1, 1, 3, 1, 1, 2], [1, 3, 1, 1, 3, 1, 1, 1, 3, 3], [1, 3, 1, 1, 2, 1, 1, 1, 2, 3]], 18),
        ]
for grid, expected in data:
    real = number_of_largest_contiguous_block(grid)
    for g in grid:
        print(g)
    print('expected {}, real {}, result {}'.format(expected, real, expected == real))
