
def remove_num(array, num):
    if array is None or len(array) == 0:
        return None

    c = r = len(array) - 1
    while True:
        while -1 < c and array[c] != num:
            c -= 1
        if c < 0:
            break
        print("before swap %s, cur[%d]=%d, remove[%d]=%d" % (array, c, array[c], r, array[r]))
        array[c] = array[r]
        array[r] = num
        print(" after swap %s, cur[%d]=%d, remove[%d]=%d" % (array, c, array[c], r, array[r]))
        c -= 1
        r -= 1
    return array[:r+1]

data = [([3, 2, 2, 3], 3, [2, 2]),
        ([0, 1, 2, 2, 3, 0, 4, 2], 2, [0, 1, 3, 0, 4]),
        ([3, 3], 3, []),
        ([3, 3], 5, [3, 3]),
        ([1, 2, 3, 4], 1, [4, 2, 3]),
        ]
for nums, val, expected in data:
    print(nums)
    real = remove_num(nums, val)
    print('{}, val {}, expected {}, real {}, result {}'.format(nums, val, expected, real, len(expected) == len(real)))
