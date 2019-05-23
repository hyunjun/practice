#   https://www.youtube.com/watch?v=cglGq7rTuPE


def closest_higher_temperatures(temps):
    if temps is None or 0 == len(temps):
        return []
    stack = [(0, temps[0])]
    i, res = 1, [0] * len(temps)
    while stack and i < len(temps):
        while stack and i < len(temps) and stack[-1][0] < i and stack[-1][1] < temps[i]:
            res[stack[-1][0]] = i - stack[-1][0]
            stack.pop()
        stack.append((i, temps[i]))
        i += 1
    while stack:
        res[stack[-1][0]] = 0
        stack.pop()
    return res


data = [([73, 74, 75, 71, 69, 72, 76, 73], [1, 1, 4, 2, 1, 1, 0, 0]),
        ([1, 2, 3, 4, 5], [1, 1, 1, 1, 0]),
        ([5, 4, 3, 2, 1], [0, 0, 0, 0, 0]),
        ([], []),
        ]
for temperatures, expected in data:
    real = closest_higher_temperatures(temperatures)
    print('{}, expected {}, real {}, result {}'.format(temperatures, expected, real, expected == real))
