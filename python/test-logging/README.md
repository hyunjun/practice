test logging
============

* test

  ```
  $ LOGGING_CONFIG_FILEPATH=common/config/logging.yaml python3 test_logging.py
  2017-08-03 23:34:49,949 [DEBUG][test_logging.py:20 -             <module>()] logging test
  $ cat logs/*
  2017-08-03 23:34:49,949 [DEBUG][test_logging.py:20 -             <module>()] logging test
  2017-08-03 23:34:49,949 [DEBUG][test_logging.py:22 -             <module>()] logging test
  ```
* requirements `pip3 install PyYAML`
