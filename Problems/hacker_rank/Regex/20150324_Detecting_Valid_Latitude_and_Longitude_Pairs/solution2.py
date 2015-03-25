import re

def is_valid_point(p):
  m = re.findall(r'\(([+-]?(0|[1-9]{1}\d*)(\.\d+)?), ([+-]?(0|[1-9]{1}\d*)(\.\d+)?)\)', p)
  if 0 < len(m):
    latitude, _, _, longitude, _, _ = m[0]
    latitude, longitude = float(latitude), float(longitude)
    if -90 <= latitude <= 90 and -180 <= longitude <= 180:
      return True
  return False

if __name__ == '__main__':
  #p = re.compile('\(([+-]?\d+(\.\d+)?), ([+-]?\d+(\.\d+)?)\)')
  N = int(raw_input())
  for i in range(N):
    if is_valid_point(raw_input()):
      print 'Valid'
    else:
      print 'Invalid'
