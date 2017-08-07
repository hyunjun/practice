# https://leetcode.com/problems/4sum/

def four_sum(nums, target):
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


nums, target = [1, 0, -1, 0, -2, 2], 0
nums, target = [-4, 0, -4, 2, 2, 2, -2, -2], 7
nums, target = [0, 0, 0, 0], 0
nums, target = [-1, 0, 1, 2, -1, -4], -1
nums, target = [-3, -2, -1, 0, 0, 1, 2, 3], 0
result = four_sum(nums, target)
for r in result:
  print(r)