import re

if __name__ == '__main__':
  strs, N = [], int(raw_input())
  [strs.append(raw_input()) for i in range(N)]
  s, p, T = ' '.join(strs), re.compile('our'), int(raw_input())
  for i in range(T):
    british_word = raw_input()
    american_word = re.sub(p, 'or', british_word)
    # https://developmentality.wordpress.com/2011/09/22/python-gotcha-word-boundaries-in-regular-expressions/
    british_pattern, american_pattern = re.compile('\\b' + british_word + '\\b'), re.compile('\\b' + american_word + '\\b')
    print len(re.findall(british_pattern, s)) + len(re.findall(american_pattern, s))

