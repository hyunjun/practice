
def qsort(l):
    if len(l) == 0:
        return []
    pivot = l[-1:][0]
    left = [i for i in l[:-1] if i <= pivot]
    right = [i for i in l[:-1] if pivot < i]
    left = qsort(left)
    right = qsort(right)
    left.append(pivot)
    left.extend(right)
    return left

data = ([3, 2, 1, 9, 4, 10, 7],
        [1, 2, 3, 4],
        [4, 3, 2, 1],
        )
for nums in data:
    expected = sorted(nums)
    real = qsort(nums)
    print('{}, expected {}, real {}, result {}'.format(nums, expected, real, expected == real))
