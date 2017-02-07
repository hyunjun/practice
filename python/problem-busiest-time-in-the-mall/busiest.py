from collections import defaultdict

#  https://www.pramp.com/question/2WBx3Axln1t7JQ2jQq96

# O(NlogN) time complexity
# O(N) space complexity
def busiest_time(data_entries):
  # aggregate same time into one
  d = defaultdict(lambda: 0)
  # time O(N)
  # space O(N)
  for item in data_entries:
    if item['type'] == 'enter':
      d[item['time']] += item['count']
    else:
      d[item['time']] -= item['count']

  # time O(NlogN)
  # space
  # sorted_data_entry = sorted(d, key=lambda t: t['time']) # sorted data
  sorted_data_entry = sorted(d.items(), key=lambda t: t[0])
  print sorted_data_entry

  cur_cnt = sorted_data_entry[0][1]
  start, end, cur_max = 0, 0, cur_cnt
  # time O(N)
  # space O(1)
  for i, cnt in enumerate([item[1] for item in sorted_data_entry]):
    if i == 0:
      continue
    if cur_cnt == 0:
      start = i
    cur_cnt += cnt
    if cur_max < cur_cnt:
      cur_max = cur_cnt
      end = i
      print (start, end, cur_max)
    if cur_cnt <= 0:
      cur_cnt = 0

  print start, end
  return (sorted_data_entry[start][0], sorted_data_entry[end][0])

# input; unsorted
# time can be multiple
# type; enter & exit
inp = [{'time': 1440084737, 'count': 4, 'type': "enter"}, {'time': 1340084737, 'count': 2, 'type': "enter"}, {'time': 1340084737, 'count': 2, 'type': "exit"}, {'time': 1440094731, 'count': 100, 'type': "enter"}, {'time': 1440084733, 'count': 5, 'type': "enter"}, {'time': 1440084834, 'count': 9, 'type': "exit"}, {'time': 1440094735, 'count': 1, 'type': "enter"}, {'time': 1440084737, 'count': 5, 'type': "exit"}, {'time': 1440084837, 'count': 9, 'type': "exit"}, {'time': 1440084637, 'count': 7, 'type': "enter"}, {'time': 1440084737, 'count': 2, 'type': "enter"}]

print busiest_time(inp)
