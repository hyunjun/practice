# https://www.interviewcake.com/question/python/stock-price


def max_profit(arr):
  min_val = arr[0]
  max_profit = 0
  for i in range(1, len(arr)):
    cur_profit = arr[i] - min_val
    if cur_profit < 0:
      min_val = arr[i]
    else:
      if max_profit < cur_profit:
        max_profit = cur_profit
  return max_profit


print(max_profit([10, 7, 5, 8, 11, 9]))
