from collections import Counter


def is_pangram(s):
  result_dict, counter_dict = {chr(i):0 for i in range(97, 97 + 26)}, Counter(s)
  del counter_dict[' ']
  for k, v in counter_dict.items():
    result_dict[k.lower()] += v
  for k, v in result_dict.items():
    if v == 0:
      return False
  return True


if __name__ == '__main__':
  if False == is_pangram(raw_input()):
    print 'not',
  print 'pangram'
