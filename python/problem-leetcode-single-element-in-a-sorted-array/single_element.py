# -*- coding: utf8 -*-
# https://leetcode.com/problems/single-element-in-a-sorted-array/#/description

def search_single_element(arr, l, r):
  if arr is None or 0 == len(arr) or r < l:
    return None
  if 1 == len(arr):
    return arr[0]

  mid = (l + r) / 2
  if 0 < mid and arr[mid - 1] != arr[mid] and mid < len(arr) - 1 and arr[mid] != arr[mid + 1]:
    return arr[mid]

  l_r = mid - 1
  while l < l_r and arr[l_r] == arr[mid]:
    l_r -= 1
  l_ret = search_single_element(arr, l, l_r)
  if l_ret is not None:
    return l_ret

  r_l = mid + 1
  while r_l < r and arr[mid] == arr[r_l]:
    r_l += 1
  r_ret = search_single_element(arr, r_l, r)
  return r_ret


def search_single_element2(arr):
  def _search_single_element(arr, l, r):
    if 1 == r - l:
      return arr[l]
    pivot = l + (r - l) / 4 * 2 # pivot을 무조건 짝수로 만들기 위한 technique

    # 문제의 조건이 단 하나만 한 번 출현하고 나머지는 두 개씩 존재한다고 하기 때문에 가능한 풀이. 멋지다
    if arr[pivot] == arr[pivot + 1]:
      return _search_single_element(arr, pivot + 2, r)
    return _search_single_element(arr, l, pivot + 1)
  return _search_single_element(arr, 0, len(arr))


arrs = [[1, 1, 2, 3, 3, 4, 4, 8, 8],
        [3, 3, 7, 7, 10, 11, 11],
        [1],
        [1, 1]]
for arr in arrs:
  l, r = 0, len(arr) - 1
  print search_single_element(arr, l, r), search_single_element2(arr)
