Redis
=====

* `test_redis.py`

  ```
  $ python3 test_redis.py
  redis version 4.0.9

  ---------- string
  english string english string True
  한글 문자열 한글 문자열 True

  ---------- dict
  {'key': 'value'} {'key': 'value'} <class 'str'> False
  {'key': 'value'} {'key': 'value'} <class 'dict'> True
  {'키': '값'} {'키': '값'} <class 'str'> False
  {'키': '값'} {'키': '값'} <class 'dict'> True

  ---------- list of dict
  [{'key': 'value'}, {'키': '값'}] [{'key': 'value'}, {'키': '값'}]

  ---------- hmset
  en_str english string <class 'str'>
  Expected object or value
  ko_str 한글 문자열 <class 'str'>
  Expected object or value
  en_dict {'key': 'value'} <class 'str'>
  Expected object or value
  ko_dict {'키': '값'} <class 'str'>
  Expected object or value
  mixed_list [{'key': 'value'}, {'키': '값'}] <class 'str'>
  Expected object or value

  ---------- hmset with json dump
  en_str english string <class 'str'>
  ko_str 한글 문자열 <class 'str'>
  en_dict {'key': 'value'} <class 'dict'>
  ko_dict {'키': '값'} <class 'dict'>
  mixed_list [{'key': 'value'}, {'키': '값'}] <class 'list'>
  ```
  * hset
    * string; 그냥 사용
    * dict, list; json dumps
  * hget
    * string; decode('utf8')
    * dict, list; json loads
  * hmset; 구분하기 귀찮으니 그냥 모든 value에 대해 json dumps
  * hgetall; 역시 구분하기 귀찮으니 decode('utf8') + json loads
  * result
    * `h*set`; json dumps
    * `hget*`; decode('utf8') + json loads

# [rq](http://python-rq.org)
* Usage

  ```
  $ pip install rq
  $ docker run -p 56379:6379 redis
  $ python3 test_rq_worker.py
  $ python3 test_rq_job.py
  ```
