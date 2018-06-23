# http://quiz.geeksforgeeks.org/quick-sort/
data = [ [4, 5, 6, 7, 8, 9, 1, 2, 3],
         [1, 2, 3, 4, 5, 6, 7, 8, 9],
         [9, 8, 7, 6, 5, 4, 3, 2, 1],
         [1, 4, 9, 8, 7, 2, 5, 3, 6]
       ]


def quicksort1(arr):
  def _quicksort(arr):
    n = len(arr) - 1
    left = [i for i in arr[0: n] if i < arr[n]]
    right = [i for i in arr[0: n] if arr[n] < i]
    sorted_arr = []
    if 0 < len(left):
      sorted_arr.extend(_quicksort(left))
    sorted_arr.append(arr[n])
    if 0 < len(right):
      sorted_arr.extend(_quicksort(right))
    return sorted_arr
  return _quicksort(arr)


for arr in data:
  print(arr, quicksort1(arr))
