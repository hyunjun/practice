# nosetests
* run

  ```
  $ nosetests
  $ nosetests -v
  $ nosetests -s

  # specific file
  $ nosetests -s tests/test_something.py

  # specific function in file
  $ nosetests -s tests/test_something.py:test_foo
  $ nosetests -s tests/test_something.py:test_bar

  # specific class in file
  $ nosetests -s tests/test_something.py:TestSomething

  # specific function in class in file
  $ nosetests -s tests/test_something.py:TestSomething.test_foo
  $ nosetests -s tests/test_something.py:TestSomething.test_bar
  ```
* ref
  * [nose](http://nose.readthedocs.org/en/latest/)
  * [pythontesting.net](http://pythontesting.net/framework/nose/)
