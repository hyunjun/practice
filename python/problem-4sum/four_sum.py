#   https://leetcode.com/problems/4sum


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


def lower_bound(nums, target):
    l, r = 0, len(nums) - 1
    while l <= r:
        m = (l + r) // 2
        if nums[m][1] == target:
            if (0 <= m - 1 and nums[m - 1][1] < target) or 0 == m:
                return m
            r -= 1
        elif nums[m][1] < target:
            l += 1
        else:
            r -= 1
    return -1


def upper_bound(nums, target):
    l, r = 0, len(nums) - 1
    while l <= r:
        m = (l + r) // 2
        if nums[m][1] == target:
            if m == r or (m + 1 <= r and target < nums[m + 1][1]):
                return m
            l += 1
        elif nums[m][1] < target:
            l += 1
        else:
            r -= 1
    return -1


#   Time Limit Exceeded
def four_sum3(nums, target):
    if nums is None or 0 == len(nums):
        return []

    nums.sort()

    len_nums, two_sum_dict = len(nums), {}
    for i in range(len_nums - 1):
        for j in range(i + 1, len_nums):
            two_sum_dict[(i, j)] = nums[i] + nums[j]

    two_sums = sorted(two_sum_dict.items(), key=lambda t: (t[1], t[0][0], t[0][1]))
    len_two_sums, result = len(two_sums), []
    #print(two_sums)
    for i in range(len_nums - 1):
        for j in range(i + 1, len_nums):
            cur_target = target - nums[i] - nums[j]
            lower_idx = lower_bound(two_sums, cur_target)
            upper_idx = upper_bound(two_sums, cur_target)
            #print(cur_target, lower_idx, upper_idx)
            if -1 == lower_idx or -1 == upper_idx:
                continue
            for k in range(lower_idx, upper_idx + 1):
                ii, jj = two_sums[k][0]
                if 4 == len(set([i, j, ii, jj])):
                    cand = sorted([nums[i], nums[j], nums[ii], nums[jj]])
                    if cand not in result:
                        result.append(cand)
    return result


class Solution:

    #   62.53%
    def fourSum(self, nums, target):
        if nums is None or 0 == len(nums):
            return []

        nums.sort()
        lenNums, twoSumDict = len(nums), {}
        for i in range(lenNums - 1):
            for j in range(i + 1, lenNums):
                curVal = nums[i] + nums[j]
                if curVal in twoSumDict:
                    twoSumDict[curVal].append((i, j))
                else:
                    twoSumDict[curVal] = [(i, j)]

        result = []
        for val, ijList in twoSumDict.items():
            curTarget = target - val
            if curTarget not in twoSumDict:
                continue
            klList = twoSumDict[curTarget]
            for i, j in ijList:
                for k, l in klList:
                    if 4 != len(set([i, j, k, l])):
                        continue
                    cand = sorted([nums[i], nums[j], nums[k], nums[l]])
                    if cand not in result:
                        result.append(cand)
        return result


from data import data
s = Solution()
for nums, target, expected in data:
    result0 = sorted(four_sum0(nums, target))
    result1 = sorted(s.fourSum(nums, target))
    print('\n', nums, target)
    print(expected)
    print(result1)
    print(sorted(expected) == result0 == result1)
