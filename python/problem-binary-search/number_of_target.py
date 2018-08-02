def lower_bound_index(nums, target):
    l, r = 0, len(nums) - 1
    while l <= r:
        m = (l + r) // 2
        if nums[m] == target:
            if m == 0 or 0 < m and nums[m - 1] < nums[m]:
                return m
            r = m - 1
        elif nums[m] < target:
            l = m + 1
        else:   #   target < nums[m]
            r = m - 1
    return -1


def upper_bound_index(nums, target):
    l, r = 0, len(nums) - 1
    while l <= r:
        m = (l + r) // 2
        if nums[m] == target:
            if m == len(nums) - 1 or m < len(nums) - 1 and nums[m] < nums[m + 1]:
                return m
            l = m + 1
        elif nums[m] < target:
            l = m + 1
        else:   #   target < nums[m]
            r = m - 1
    return -1


def get_count(nums, target):
    if nums is None or 0 == len(nums):
        return 0
    lower_bound_idx = lower_bound_index(nums, target)
    upper_bound_idx = upper_bound_index(nums, target)
    if -1 == lower_bound_idx or -1 == upper_bound_idx:
        return 0
    return upper_bound_idx - lower_bound_idx + 1


nums = [-5, -1, -1, -1, 1, 4, 4, 6] #   allow duplication


lower_bound_cases = [(-6, -1), (-5, 0), (-3, -1), (-1, 1), (0, -1), (1, 4), (2, -1), (4, 5), (5, -1), (6, 7), (7, -1)]
print('\nlower bound test\tnums {}'.format(nums))
for target, expected in lower_bound_cases:
    real = lower_bound_index(nums, target)
    print('target {}\texpected {}\treal {}\tresult {}'.format(target, expected, real, expected == real))


upper_bound_cases = [(-6, -1), (-5, 0), (-3, -1), (-1, 3), (0, -1), (1, 4), (2, -1), (4, 6), (5, -1), (6, 7), (7, -1)]
print('\nupper bound test\tnums {}'.format(nums))
for target, expected in upper_bound_cases:
    real = upper_bound_index(nums, target)
    print('target {}\texpected {}\treal {}\tresult {}'.format(target, expected, real, expected == real))


get_count_cases = [(-6, 0), (-5, 1), (-3, 0), (-1, 3), (0, 0), (1, 1), (2, 0), (4, 2), (5, 0), (6, 1), (7, 0)]
print('\ntest get count\tnums {}'.format(nums))
for target, expected in get_count_cases:
    real = get_count(nums, target)
    print('target {}\texpected {}\treal {}\tresult {}'.format(target, expected, real, expected == real))
