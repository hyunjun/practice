import re
import timeit


hangul_re = re.compile(r"[ㄱ-ㅎ|가-힇]")


def is_hangul(text):
  return hangul_re.search(text) is not None


def is_hangul_old(text):
  hangul = re.compile('[\u3131-\u3163\uac00-\ud7a3]+')
  result = hangul.findall(text)
  return len(result)


hangul = re.compile('[\u3131-\u3163\uac00-\ud7a3]+')


def is_hangul_old2(text):
  return hangul.search(text) is not None


for w in ['한글', 'abcd', 'abcd한글']:
  print('{}\t{}\t{}\t{}'.format(w, is_hangul(w), is_hangul_old(w), is_hangul_old2(w)))


text = '한글 한글 한글'
print(timeit.timeit('is_hangul(text)', setup='from __main__ import is_hangul, text'))
print(timeit.timeit('is_hangul_old(text)', setup='from __main__ import is_hangul_old, text'))
print(timeit.timeit('is_hangul_old2(text)', setup='from __main__ import is_hangul_old2, hangul, text'))
