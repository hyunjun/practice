#   http://blog.kjslab.com/122


def pick_four(nums, target):
    if nums is None or 0 == len(nums):
        return []
    #   O(nlogn)
    nums.sort()

    len_nums, two_sum_dict = len(nums), {}
    #   O(n^2)
    for i in range(len_nums):
        for j in range(len_nums):
            two_sum_dict[nums[i] + nums[j]] = (i, j)

    two_sums = sorted(two_sum_dict.items(), key=lambda t: t[0])
    l, r, result = 0, len(two_sums) - 1, []
    #   O(n^2logn^2) -> O(n^2logn)
    while l < r:
        cur_val = two_sums[l][0] + two_sums[r][0]
        if cur_val == target:
            l1, l2 = two_sums[l][1]
            r1, r2 = two_sums[r][1]
            cand = sorted([nums[l1], nums[l2], nums[r1], nums[r2]])
            if cand not in result:
                result.append(cand)
            l += 1
            r -= 1
        elif cur_val < target:
            l += 1
        else:
            r -= 1
    return result


print(pick_four([1, 4, 3], 9))
