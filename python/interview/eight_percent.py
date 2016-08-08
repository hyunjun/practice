# https://brunch.co.kr/@sunghokimnxag/5

def pingpong_loop(x):
  num, direction = 0, True
  for i in range(1, x + 1):
    if direction:
      num += 1
    else:
      num -= 1
    if i % 7 == 0 or '7' in str(i):
      direction = not direction
  return num

def pingpong_recursive(x):
  def _pingpong_recursive(cur, num, direction):
    if x == cur:
      return num
    if cur % 7 == 0 or '7' in str(cur):
      direction = not direction
    if direction:
      return _pingpong_recursive(cur + 1, num + 1, direction)
    else:
      return _pingpong_recursive(cur + 1, num - 1, direction)
  return _pingpong_recursive(1, 1, True)

expected_list = [1, 7, 6, 0, 1, 3, 2, -1, 0]
for i, num in enumerate([1, 7, 8, 14, 15, 17, 18, 21, 22]):
  print num, pingpong_loop(num), expected_list[i], pingpong_recursive(num)
