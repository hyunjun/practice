# -*- coding: utf8 -*-
from keystroke import *


def test_jamo2eng():
  assert u'r' == jamo2eng(u'ㄱ')
  assert u'.' == jamo2eng(u'.')


def test_kor_char2jamos():
  assert (u'ㅌ', u'ㅔ', u'') == kor_char2jamos(u'테')


def test_string2keystrokes():
  assert None == string2keystrokes(None)
  assert u'' == string2keystrokes('')

  assert u'xptmxm' == string2keystrokes('ㅌㅔ스트')
  assert u'xptmxm' == string2keystrokes('테스트')
  assert u'xptmxm' == string2keystrokes(u'ㅌㅔ스트')
  assert u'xptmxm' == string2keystrokes(u'테스트')
          
  assert u'xptmxm ab gkgk gl 012zz Rr9xrt"' == string2keystrokes('테스트 ab 하하 ㅎㅣ 012ㅋㅋ ㄲㄱ9ㅌㄱㅅ"')
  assert u'xptmxm ab gkgk gl 012zz Rr9xrt"' == string2keystrokes(u'테스트 ab 하하 ㅎㅣ 012ㅋㅋ ㄲㄱ9ㅌㄱㅅ"')

  assert u'xptmxm ab gl µ ⑥ ズQyfx ↗ 龍 ✊' == string2keystrokes(u'테스트 ab ㅎㅣ µ ⑥ ズ뾽 ↗ 龍 ✊')
