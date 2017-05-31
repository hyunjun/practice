# problem of yunmok
# https://www.codeground.org/practice/practiceProblemView 윤목의 달인

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
    ret = get_nums(tmp_nums, target_sum - cur_num * i, cur_num - 1, cur_cnt - i)
    if ret != []:
      return ret
  return []

def get_nums2(n5, n4, n3, n2, n1, target_sum, cnt):
  if n5 + n4 + n3 + n2 + n1 < cnt:
    r5 = get_nums2(n5 + 1, n4, n3, n2, n1, target_sum, cnt)
    if r5 != []:
      return r5
    r4 = get_nums2(n5, n4 + 1, n3, n2, n1, target_sum, cnt)
    if r4 != []:
      return r4
    r3 = get_nums2(n5, n4, n3 + 1, n2, n1, target_sum, cnt)
    if r3 != []:
      return r3
    r2 = get_nums2(n5, n4, n3, n2 + 1, n1, target_sum, cnt)
    if r2 != []:
      return r2
    r1 = get_nums2(n5, n4, n3, n2, n1 + 1, target_sum, cnt)
    if r1 != []:
      return r1
  elif n5 + n4 + n3 + n2 + n1 == cnt:
    if n5 * 5 + n4 * 4 + n3 * 3 + n2 * 2 + n1 * 1 == target_sum:
      return [n5, n4, n3, n2, n1]
  return []

def get_nums3(target_sum, cnt):
  n5 = min((int) (target_sum / 5), cnt)
  n4 = min((int) (target_sum / 4), cnt)
  n3 = min((int) (target_sum / 3), cnt)
  n2 = min((int) (target_sum / 2), cnt)
  n1 = min((int) (target_sum / 1), cnt)
  for i5 in range(n5, -1, -1):
    if i5 == cnt:
      if i5 * 5 == target_sum:
        return [i5, 0, 0, 0, 0]
    for i4 in range(n4, -1, -1):
      if i5 + i4 > cnt:
        continue
      elif i5 + i4 == cnt:
        if i5 * 5 + i4 * 4 == target_sum:
          return [i5, i4, 0, 0, 0]
      for i3 in range(n3, -1, -1):
        if i5 + i4 + i3 > cnt:
          continue
        if i5 + i4 + i3 == cnt:
          if i5 * 5 + i4 * 4 + i3 * 3 == target_sum:
            return [i5, i4, i3, 0, 0]
        for i2 in range(n2, -1, -1):
          if i5 + i4 + i3 + i2 > cnt:
            continue
          if i5 + i4 + i3 + i2 == cnt:
            if i5 * 5 + i4 * 4 + i3 * 3 + i2 * 2 == target_sum:
              return [i5, i4, i3, i2, 0]
          for i1 in range(n1, -1, -1):
            if i5 + i4 + i3 + i2 + i1 > cnt:
              continue
            if i5 + i4 + i3 + i2 + i1 == cnt:
              if i5 * 5 + i4 * 4 + i3 * 3 + i2 * 2 + i1 * 1 == target_sum:
                return [i5, i4, i3, i2, i1]
  return []


for i in [5.0, 4.5, 3.2]:
  cnt = get_count(i)
  target_sum = cnt * i
  print i, cnt, target_sum, get_nums([0, 0, 0, 0, 0], target_sum, 5, cnt), get_nums2(0, 0, 0, 0, 0, target_sum, cnt), get_nums3(target_sum, cnt)

  target_sum = (int) (target_sum)
  target_sum -= cnt
  nums = [0, 0, 0, 0, target_sum / 4]
  target_sum %= 4
  if target_sum > 0:
    nums[target_sum] += 1
  nums[0] = cnt - nums[1] - nums[2] - nums[3] - nums[4]
  print nums
