* objective
  * test of writing a compressed file when downloading it using zlib
* test

  ```
  ❯ time python3 -m memory_profiler download.py
  ❯ time python3 -m memory_profiler download_zlib.py
  ```
* downloaded files

  ```
  ❯ md5 /tmp/test100Mb.db /tmp/test100Mb.zlib.db ~/Downloads/test100Mb.db
  MD5 (/tmp/test100Mb.db) = 2f282b84e7e608d5852449ed940bfc51
  MD5 (/tmp/test100Mb.zlib.db) = 2f282b84e7e608d5852449ed940bfc51
  MD5 (/Users/<user>/Downloads/test100Mb.db) = 2f282b84e7e608d5852449ed940bfc51
  ```
* ref
  * https://docs.python.org/ko/3/library/zlib.html
  * https://blackcon.tistory.com/148
  * https://smothly.github.io/programming%20language/python/2020/03/13/Python-Memory-%EC%82%AC%EC%9A%A9%EB%9F%89-%EC%B8%A1%EC%A0%95%ED%95%98%EA%B8%B0.html
  * [zlib - Compress data from a stream and send to another stream to decompress - Python code example - Kite](https://www.kite.com/python/examples/1940/zlib-compress-data-from-a-stream-and-send-to-another-stream-to-decompress)
  * [gzip-stream: Streaming GZIP compression for Python](https://github.com/leenr/gzip-stream)
