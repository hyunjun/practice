#   https://www.geeksforgeeks.org/remove-minimum-elements-from-either-side-such-that-2min-becomes-more-than-max-set-2


def remove_minimum_elements(nums):
    if nums is None or 0 == len(nums):
        return 0
    s, e, min_num, max_num, max_cnt = 0, 0, nums[0], nums[0], 1
    for i, n in enumerate(nums):
        min_num = min(min_num, n)
        max_num = max(max_num, n)
        if min_num * 2 > max_num:
            e = i
        else:
            s = e = i
            min_num = max_num = n
        max_cnt = max(max_cnt, e - s + 1)
    return len(nums) - max_cnt


data = [([4, 5, 100, 9, 10, 11, 12, 15, 200], 4),
        ([4, 7, 5, 6], 0),
        ([20, 7, 5, 6], 1),
        ]
for nums, expected in data:
    real = remove_minimum_elements(nums)
    print('{}, expected {}, real {}, result {}'.format(nums, expected, real, expected == real))
