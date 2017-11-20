def lower_bound(nums, target):
    l, r = 0, len(nums) - 1
    if target == nums[l]:
        return l
    if target == nums[r]:
        return r
    while l < r:
        m = (int)((l + r) / 2)
        if nums[m] == target:
            return m
        elif nums[m] < target:
            l = m + 1
            if target < nums[l]:
                return m
        else:   #   target < nums[m]
            r = m - 1
            if nums[r] <= target:
                return r
    return -1


nums = [-5, -1, 1, 4]
cases = [(-6, -1), (-5, 0), (-3, 0), (-1, 1), (0, 1), (1, 2), (2, 2), (4, 3), (5, -1)]
print('nums {}'.format(nums))
for target, expected in cases:
    real = lower_bound(nums, target)
    print('target {}\texpected {}\treal {}\tresult {}'.format(target, expected, real, expected == real))
