Docker Memory Overflow
======================

* Simple example using string append

  ```
  $ docker run --rm -m 32m -it python python
  Python 3.6.3 (default, Nov  4 2017, 22:17:09)
  [GCC 4.9.2] on linux
  Type "help", "copyright", "credits" or "license" for more information.
  >>> s = 'test'
  >>> for i in range(25):
  ...   s += s
  ...
  $ # memory overflow로 강제 종료
  ```
* Execute

  ```
  $ mkdir log
  $ ./build_and_execute.sh
  ...

  root@45f491834cb7:/test# python3 test_ok.py
  ...
  2017-11-29 04:30:36,500.500 DEBUG test_ok - my_func: TEST
  2017-11-29 04:30:36,500.500 DEBUG test_ok - my_func: TEST
  ...

  root@45f491834cb7:/test# python3 test_overflow.py 2>> /logs/log.test
  ```
  * docker stats로 memory를 보면
  * docker 17.03.1-ce + CentOS Linux release 7.3.1611 (Core) 에서 memory가 가득 참
  * docker 17.09.0-ce + macOS Sierra에서는 아무 문제 없음
