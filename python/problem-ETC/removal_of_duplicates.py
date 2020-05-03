#   https://codebasil.com/problems/inplace-removal-of-duplicates


def removeDuplicatesInPlace(array):
    for i in range(1, len(array)):
        if array[i - 1] == array[i]:
            array[i - 1] = None
    n = 0
    while n < len(array) and array[n] is not None:
        n += 1
    if n == len(array):
        return array
    for i in range(n + 1, len(array)):
        if array[i]:
            array[n] = array[i]
            n += 1
    for i in range(n, len(array)):
        array[i] = None
        return array[:n]


data = [([1, 1, 2, 3, 4, 4, 4, 5], [1, 2, 3, 4, 5]),
        ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),
        ([12, 14, 15, 15, 17, 17, 17, 18], [12, 14, 15, 17, 18]),
        ]
for array, expected in data:
    real = removeDuplicatesInPlace(array)
    print(f'{array} expected {expected} real {real} result {expected == real}')
