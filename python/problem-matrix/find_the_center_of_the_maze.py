#   https://codebasil.com/problems/find-the-center-of-the-maze

#   spiral matrix 문제


def findTheCenterOfTheMaze(maze):
    if maze is None or 0 == len(maze) or 0 == len(maze[0]):
        return []

    def getDir(_dir):
        _dir <<= 1
        if 16 == _dir:
            _dir = 1
        return _dir

    R, C, visited = len(maze), len(maze[0]), set()
    def isPerimeter(_dir, r, c):
        if 1 == _dir:
            if c + 1 == C or (r, c + 1) in visited:
                return True
        elif 2 == _dir:
            if r + 1 == R or (r + 1, c) in visited:
                return True
        elif 4 == _dir:
            if c - 1 == -1 or (r, c - 1) in visited:
                return True
        elif 8 == _dir:
            if r - 1 == -1 or (r - 1, c) in visited:
                return True
        return False

    _dir, r, c, res = 1, 0, 0, []
    while len(visited) < R * C:
        if isPerimeter(_dir, r, c):
            _dir = getDir(_dir)
        visited.add((r, c))
        res.append(maze[r][c])
        if _dir == 1:
            c += 1
        elif _dir == 2:
            r += 1
        elif _dir == 4:
            c -= 1
        elif _dir == 8:
            r -= 1
    return res


data = [([[23, 17, 34, 5], [1, 9, 12, 14], [8, 2, 3, 16]], [23, 17, 34, 5, 14, 16, 3, 2, 8, 1, 9, 12]),
        ]
for maze, expected in data:
    real = findTheCenterOfTheMaze(maze)
    for m in maze:
        print(m)
    print(f'expected {expected}, real {real}, result {expected == real}')
