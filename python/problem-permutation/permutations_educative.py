#   https://www.educative.io/collection/page/5668639101419520/5671464854355968/5720758194012160


def find_permutations(nums):
    if nums is None or 0 == len(nums):
        return []
    res = [nums]
    for i in range(len(nums)):
        tmp = []
        for j in range(i + 1, len(nums)):
            for r in res:
                t = r[:]
                t[i], t[j] = t[j], t[i]
                tmp.append(t)
        res.extend(tmp)
    return res


data = [([1, 3, 5], [[1,3,5], [1,5,3], [3,1,5], [3,5,1], [5,1,3], [5,3,1]]),
        ]
for nums, expected in data:
    real = find_permutations(nums)
    print('{}, expected {}, real {}, result {}'.format(nums, expected, real, sorted(expected) == sorted(real)))
