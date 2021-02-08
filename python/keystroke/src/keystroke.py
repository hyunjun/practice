# -*- coding: utf8 -*-


jamo2eng_dict =  {
  # chosung (consonants)
  u'ㄱ':u'r', u'ㄲ':u'R', u'ㄴ':u's', u'ㄷ':u'e', u'ㄸ':u'E',
  u'ㄹ':u'f', u'ㅁ':u'a', u'ㅂ':u'q', u'ㅃ':u'Q', u'ㅅ':u't',
  u'ㅆ':u'T', u'ㅇ':u'd', u'ㅈ':u'w', u'ㅉ':u'W', u'ㅊ':u'c',
  u'ㅋ':u'z', u'ㅌ':u'x', u'ㅍ':u'v', u'ㅎ':u'g',
  # jungsung (vowels)
  u'ㅏ':u'k', u'ㅐ':u'o', u'ㅑ':u'i', u'ㅒ':u'O', u'ㅓ':u'j',
  u'ㅔ':u'p', u'ㅕ':u'u', u'ㅖ':u'P', u'ㅗ':u'h', u'ㅘ':u'hk',
  u'ㅙ':u'ho', u'ㅚ':u'hl', u'ㅛ':u'y', u'ㅜ':u'n', u'ㅝ':u'nj',
  u'ㅞ':u'np', u'ㅟ':u'nl', u'ㅠ':u'b', u'ㅡ':u'm', u'ㅢ':u'ml',
  u'ㅣ':u'l',
  # jongsung (consonants)
  u'':u'', u'ㄳ':u'rt', u'ㄵ':u'sw', u'ㄶ':u'sg', u'ㄺ':u'fr',
  u'ㄻ':u'fa', u'ㄼ':u'fq', u'ㄽ':u'ft', u'ㄾ':u'fx', u'ㄿ':u'fv',
  u'ㅀ':u'fg', u'ㅄ':u'qt',
  }


# Hangul Compatibility Jamo
# http://jrgraphix.net/r/Unicode/3130-318F
chosungs = [  # 0x3131 - 0x314E
  u'ㄱ', u'ㄲ', u'ㄴ', u'ㄷ', u'ㄸ',
  u'ㄹ', u'ㅁ', u'ㅂ', u'ㅃ', u'ㅅ',
  u'ㅆ', u'ㅇ', u'ㅈ', u'ㅉ', u'ㅊ',
  u'ㅋ', u'ㅌ', u'ㅍ', u'ㅎ'
  ]


jungsungs = [ # 0x314F - 0x3163
  u'ㅏ', u'ㅐ', u'ㅑ', u'ㅒ', u'ㅓ',
  u'ㅔ', u'ㅕ', u'ㅖ', u'ㅗ', u'ㅘ',
  u'ㅙ', u'ㅚ', u'ㅛ', u'ㅜ', u'ㅝ',
  u'ㅞ', u'ㅟ', u'ㅠ', u'ㅡ', u'ㅢ',
  u'ㅣ'
  ]


jongsungs = [
  u'',   u'ㄱ', u'ㄲ', u'ㄳ', u'ㄴ',
  u'ㄵ', u'ㄶ', u'ㄷ', u'ㄹ', u'ㄺ',
  u'ㄻ', u'ㄼ', u'ㄽ', u'ㄾ', u'ㄿ',
  u'ㅀ', u'ㅁ', u'ㅂ', u'ㅄ', u'ㅅ',
  u'ㅆ', u'ㅇ', u'ㅈ', u'ㅊ', u'ㅋ',
  u'ㅌ', u'ㅍ', u'ㅎ'
  ]


def jamo2eng(jamo):
  return jamo2eng_dict[jamo] if jamo in jamo2eng_dict else jamo


def kor_char2jamos(char):
  code = ord(char)

  # Hangul Syllables
  # http://jrgraphix.net/r/Unicode/AC00-D7AF
  if 0xAC00 <= code <= 0xD7A3:   # A full character
    basecode = code - 0xAC00
    jongsung_idx = basecode % 28
    jungsung_idx = (basecode / 28) % 21
    chosung_idx = ((basecode / 28) / 21) % 19
    return (chosungs[chosung_idx], jungsungs[jungsung_idx], jongsungs[jongsung_idx])

  return ( "", "", "" )


def string2keystrokes(s):
  if s is None:
    return None

  if isinstance(s, str):
    s = unicode(s, 'utf8')

  result = []
  for c in s:
    if c in jamo2eng_dict:
      result.append(jamo2eng_dict[c])
      continue

    chosung, jungsung, jongsung = kor_char2jamos( c )
    if '' != chosung or '' != jungsung or '' != jongsung:
      result.extend([jamo2eng(chosung), jamo2eng(jungsung), jamo2eng(jongsung)])
      continue

    result.append(c)

  return ''.join(result)


if __name__ == '__main__':
  pass
