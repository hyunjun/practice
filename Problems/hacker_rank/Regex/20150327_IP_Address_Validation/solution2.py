import re

p_ipv4 = re.compile('^(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})$')
def is_ipv4(s):
  m = re.findall(p_ipv4, s)
  if 0 < len(m):
    #if '.'.join(m[0]) != s:
    #  return False
    for n in m[0]:
      num = int(n)
      if 255 < num or str(num) != n:  # to prevent such as 012.x.y.z
        return False
    return True
  return False

p_ipv6 = re.compile('^[\da-f]{1,4}(:[\da-f]{1,4}){7}$')
def is_ipv6(s):
  m = re.match(p_ipv6, s)
  if m is not None:
    if m.group() == s:
      return True
  return False

if __name__ == '__main__':
  N = int(raw_input())
  for i in range(N):
    s = raw_input()
    if is_ipv4(s):
      print 'IPv4'
    elif is_ipv6(s):
      print 'IPv6'
    else:
      print 'Neither'
