#   move all targets at the rightmost of nums


def move_targets(nums, target):
    if nums is None or 0 == len(nums):
        return 0
    i = 0
    for j in range(len(nums)):
        if target != nums[j]:
            nums[i] = nums[j]
            i += 1
    for j in range(i, len(nums)):
        nums[j] = target
    return i


data = [([3, 2, 2, 3], 3, [2, 2, 3, 3]),
        ([0, 1, 2, 2, 3, 0, 4, 2], 2, [0, 1, 3, 0, 4, 2, 2, 2]),
        ([3, 3], 5, [3, 3]),
        ([1, 2, 3, 4], 1, [2, 3, 4, 1]),
        ([0, 2, 4, 0, 7], 0, [2, 4, 7, 0, 0]),
        ]
for nums, target, expected in data:
    print(nums)
    real = move_targets(nums, target)
    print('\ttarget {}, expected {}, result {}'.format(target, expected, expected == nums))
