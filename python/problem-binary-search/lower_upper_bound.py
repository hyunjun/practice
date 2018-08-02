#   https://codingblocks.com/resources/binary-search-upper-lower-bound/
#   http://thushw.blogspot.com/2010/07/why-am-i-writing-lowerbound-in-java.html


def lower_bound(nums, target):
    l, r = 0, len(nums) - 1
    if target == nums[l]:
        return l
    if nums[r] <= target:
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


def lower_bound1(nums, target):
    l, r = 0, len(nums) - 1
    if target == nums[l]:
        return l
    if nums[r] <= target:
        return r
    while l <= r:
        m = (l + r) // 2
        if nums[m] <= target < nums[m + 1]:
            return m
        elif target < nums[m]:
            r = m - 1
        else:   #   target < nums[m]
            l = m + 1
    return -1


def upper_bound(nums, target):
    l, r = 0, len(nums) - 1
    if target <= nums[l]:
        return l
    if target == nums[r]:
        return r
    while l < r:
        m = (int)((l + r) / 2)
        if nums[m] == target:
            return m
        elif nums[m] < target:
            l = m + 1
            if target <= nums[l]:
                return l
        else:   #   target < nums[m]
            r = m - 1
            if nums[r] < target:
                return m
    return -1


def upper_bound1(nums, target):
    l, r = 0, len(nums) - 1
    if target <= nums[l]:
        return l
    if target == nums[r]:
        return r
    while l <= r:
        m = (l + r) // 2
        if nums[m - 1] < target <= nums[m]:
            return m
        elif nums[m] < target:
            l = m + 1
        else:
            r = m - 1
    return -1


nums = [-5, -1, 1, 4]


lower_bound_cases = [(-6, -1), (-5, 0), (-3, 0), (-1, 1), (0, 1), (1, 2), (2, 2), (4, 3), (5, 3)]
print('lower bound test\tnums {}'.format(nums))
for target, expected in lower_bound_cases:
    real = lower_bound(nums, target)
    real1 = lower_bound1(nums, target)
    print('target {}\texpected {}\treal {}\treal1 {}\tresult {}'.format(target, expected, real, real1, expected == real == real1))


upper_bound_cases = [(-6, 0), (-5, 0), (-3, 1), (-1, 1), (0, 2), (1, 2), (2, 3), (4, 3), (5, -1)]
print('\nupper bound test\tnums {}'.format(nums))
for target, expected in upper_bound_cases:
    real = upper_bound(nums, target)
    real1 = upper_bound1(nums, target)
    print('target {}\texpected {}\treal {}\treal1 {}\tresult {}'.format(target, expected, real, real1, expected == real == real1))
