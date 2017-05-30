# problem of yunmok

def get_count(avg):
  cnt = 1
  while True:
    cand = (int) (cnt * avg)
    if cand - cnt * avg == 0:
      return cnt
    cnt += 1
  return 0


def get_nums(nums, target_sum, cur_num, cur_cnt):
  # print nums, target_sum, cur_num, cur_cnt
  if cur_num == 0 or cur_cnt == 0:
    return []

  cand_cnt = cur_cnt

  if target_sum - cur_num * cand_cnt == 0:
    nums[cur_num - 1] = cand_cnt
    return nums

  if cand_cnt == 1 and target_sum < cur_num * cand_cnt:
    return []

  if target_sum == 0 and cand_cnt > 0:
    return []

  while target_sum < cur_num * cand_cnt:
    cand_cnt -= 1

  for i in range(cand_cnt, -1, -1):
    tmp_nums = nums[:]
    tmp_nums[cur_num - 1] = i
    ret = get_nums(tmp_nums, target_sum - cur_num * i, cur_num - 1, cur_num - i)
    if ret != []:
      return ret
  return []

for i in [5.0, 4.5, 3.2]:
  cnt = get_count(i)
  target_sum = cnt * i
  print i, cnt, target_sum, get_nums([0, 0, 0, 0, 0], target_sum, 5, cnt)
