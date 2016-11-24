# Screening question
* Execution

  ```
  $ python --version
  Python 2.7.10

  $ nosetests -v
  test_merge.test_list_len ... ok
  test_merge.test_merge_case_none ... ok
  test_merge.test_merge ... ok
  
  ----------------------------------------------------------------------
  Ran 3 tests in 0.002s
  
  OK

  $ python src/merge.py
  [0] [0] [1] [1] [2] [3]
  ``` 
* Installation of nosetests

  ```
  $ sudo easy_install nose
  ``` 
