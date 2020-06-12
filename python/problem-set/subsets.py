#   https://www.educative.io/collection/page/5668639101419520/5671464854355968/5670249378611200


def subsets(nums):
    if nums is None or 0 == len(nums):
        return [[]]
    res = []
    for i in range(2 ** len(nums)):
        indices = []
        for j in range(31, -1, -1):
            if (2 ** j) & i:
                indices.append(j)
        res.append([nums[i] for i in sorted(indices)])
    return res


data = [([1, 3], [[], [1], [3], [1, 3]]),
        ([1, 5, 3], [[], [1], [5], [3], [1, 5], [1, 3], [5, 3], [1, 5, 3]]),
        ]
for nums, expected in data:
    real = subsets(nums)
    print('{}, expected {}, real {}, result {}'.format(nums, expected, real, sorted(expected) == sorted(real)))
