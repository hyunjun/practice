import sys

def get_max_profit(prices):
    max_profit = 0
    if prices is None or 0 == len(prices):
        return max_profit
    _min, _max = sys.maxsize, -sys.maxsize
    for p in prices:
        if p < _min:
            _min = _max = p
        elif _max < p:
            _max = p
            if 0 < _max - _min and max_profit < _max - _min:
                max_profit = _max - _min
    return max_profit


data = [[10, 20, 30, 40, 50],
        [23, 55, 67, 22, 40, 65, 44, 20],
        [25, 30, 48, 15, 25, 45, 10, 25],
        [],
        [1, 1, 1, 1],
        [10, 9, 8, 7],
        [10, 7, 5, 8, 11, 9],
        ]
for prices in data:
    print(prices, get_max_profit(prices))
