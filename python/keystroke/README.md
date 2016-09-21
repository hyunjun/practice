Keystroke
=========
* 입력을 keystroke로 변환하는 파이썬 코드
  * 입력은 utf8, unicode 두 가지 다 받지만, 출력은 unicode만 지원
* Usage (Python 2.7)

  ```
  $ python
  >>> from keystroke import *
  >>> string2keystrokes('ㅌㅔ스트')
  u'xptmxm'
  ```
* Test

  ```
  $ nosetests -v
  test_keystroke.test_jamo2eng ... ok
  test_keystroke.test_kor_char2jamos ... ok
  test_keystroke.test_string2keystrokes ... ok

  ----------------------------------------------------------------------
  Ran 3 tests in 0.003s

  OK
  ```
  * installation nose on OS X

    ```
    # if pip is not installed
    $ sudo easy_install pip
    $ sudo pip install --upgrade pip
    $ sudo pip install nose
    ```
