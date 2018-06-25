#   https://leetcode.com/problems/4sum/


#   32.21%
def four_sum0(nums, target):
    nums.sort()
    #print('sorted {}'.format(nums))
    len_nums = len(nums)
    result = []
    for i in range(len_nums - 3):
        if 0 < i and nums[i - 1] == nums[i]:
            continue
        for j in range(i + 1, len_nums - 2):
            target_2sum = target - nums[i] - nums[j]
            #print('[{}] {}\t[{}] {}\ttarget 2sum = {}'.format(i, nums[i], j, nums[j], target_2sum))
            l, r = j + 1, len_nums - 1
            while l < r:
                cur_sum = nums[l] + nums[r]
                if target_2sum == cur_sum:
                    tmp_result = [nums[i], nums[j], nums[l], nums[r]]
                    if tmp_result not in result:
                        result.append(tmp_result)
                    l += 1
                    r -= 1
                elif target_2sum < cur_sum:
                    while l < r and nums[r - 1] == nums[r]:
                        r -= 1
                    r -= 1
                else:
                    while l < r and nums[l] == nums[l + 1]:
                        l += 1
                    l += 1
    return result


#   Time Limit Exceeded
def four_sum1(nums, target):
    def four_sum_recur(nums, acc):
        if 4 == len(acc):
            if target == sum(acc):
                acc = sorted(acc)
                if acc not in result:
                    result.append(acc[:])
            return
        for i, n in enumerate(nums):
            acc.append(n)
            four_sum_recur(nums[:i] + nums[i + 1:], acc)
            acc.pop()

    if nums is None or 0 == len(nums):
        return []

    nums.sort()
    result = []
    four_sum_recur(nums, [])
    return result


#   Time Limit Exceeded
def four_sum2(nums, target):
    if nums is None or 0 == len(nums):
        return []

    len_nums, two_sum_dict = len(nums), {}
    for i in range(len_nums - 1):
        for j in range(i + 1, len_nums):
            two_sum_dict[(i, j)] = nums[i] + nums[j]

    counter_dict = {}
    for n in nums:
        if n in counter_dict:
            counter_dict[n] += 1
        else:
            counter_dict[n] = 1

    result = []
    for i, ((n1, n2), val1) in enumerate(two_sum_dict.items()):
        for j, ((n3, n4), val2) in enumerate(two_sum_dict.items()):
            if j <= i:
                continue
            if target != val1 + val2:
                continue
            cand = sorted([nums[n1], nums[n2], nums[n3], nums[n4]])
            if cand in result:
                continue
            cand_counter_dict = {}
            for c in cand:
                if c in cand_counter_dict:
                    cand_counter_dict[c] += 1
                else:
                    cand_counter_dict[c] = 1
            is_valid = True
            for c, cnt in cand_counter_dict.items():
                if counter_dict[c] < cnt:
                    is_valid = False
                    break
            if is_valid:
                result.append(cand)
    return result


from data import data
for nums, target, expected in data:
    result0 = sorted(four_sum0(nums, target))
    result1 = sorted(four_sum1(nums, target))
    result2 = sorted(four_sum2(nums, target))
    print(nums, target)
    print(expected)
    print(sorted(expected) == result0 == result1 == result2)
