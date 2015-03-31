import re

if __name__ == '__main__':
  lines, N = [], int(raw_input())
  [lines.append(raw_input()) for i in range(N)]
  line = ' '.join(lines)
  cnt, test_cases, p, T = 0, [], re.compile('ze$'), int(raw_input())
  for i in range(T):
    american = raw_input()
    british = re.sub(p, 'se', american)
    p_american, p_british = re.compile(american), re.compile(british)
    c_american, c_british = len(re.findall(p_american, line)), len(re.findall(p_british, line))
    print c_american + c_british
