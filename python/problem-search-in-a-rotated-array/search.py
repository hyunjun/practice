# http://www.practice.geeksforgeeks.org/problem-page.php?pid=146
# http://www.geeksforgeeks.org/search-an-element-in-a-sorted-and-pivoted-array/

# arr, target number, answer index
data = [([5, 6, 7, 8, 9, 10, 1, 2, 3], 10, 5),
        ([5, 6, 7, 8, 9, 10, 1, 2, 3], 3, 8),
        ([4, 5, 6, 7, 8, 9, 1, 2, 3], 6, 2),
        ([3, 1, 2], 1, 1),
        ([3, 5, 1, 2], 6, -1),
        ([3, 4, 5, 1, 2], 1, 3)]

def search(arr, n):
  l, r = 0, len(arr) - 1
  while l <= r:
    i = (l + r) / 2
    if arr[i] == n:
      return i
    if arr[l] < arr[i]: # ascending left, rotating right
      if arr[l] <= n < arr[i]:  # target in ascending left
        r = i - 1
      else:
        l = i + 1
    else: # arr[i] < arr[r] # rotating left, ascending right
      if arr[i] < n <= arr[r]:  # target in ascending right
        l = i + 1
      else:
        r = i - 1
  return -1

for arr, n, i in data:
  answer = search(arr, n)
  print arr, n, i, answer, i == answer
