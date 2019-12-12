cost = [[0, 10, 75, 94],
        [-1, 0, 35, 50],
        [-1, -1, 0, 80],
        [-1, -1, -1, 0],
        ]


def minCost(cost, s, d):
    if d == s:
        return 0
    if d - s == 1:
        return cost[s][d]
    minRes = cost[s][d]
    for i in range(s + 1, d):
        minRes = min(minCost(cost, s, i) + minCost(cost, i, d), minRes)
    return minRes


print(minCost(cost, 0, 2))
print(minCost(cost, 0, 3))
