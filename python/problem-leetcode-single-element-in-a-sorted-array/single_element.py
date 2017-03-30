# https://leetcode.com/problems/single-element-in-a-sorted-array/#/description

def search_single_element(arr, l, r):
  if arr is None or 0 == len(arr) or r < l:
    return None

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

arr = [1, 1, 2, 3, 3, 4, 4, 8, 8]
l, r = 0, len(arr) - 1
print search_single_element(arr, l, r)
arr = [3, 3, 7, 7, 10, 11, 11]
l, r = 0, len(arr) - 1
print search_single_element(arr, l, r)
