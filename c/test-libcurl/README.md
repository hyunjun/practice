Test libcurl
============

* Compile
  * [how to install curl and libcurl](https://curl.haxx.se/docs/install.html)
  * `gcc test_libcurl.c -g -lcurl` on `CentOS Linux release 7.3.1611 (Core)`
  * `gcc test_libcurl.c -g -lcurl` on `macOS 10.12.5 (16F73)`
   * [gcc won't include libcurl on commandline for OS X](https://stackoverflow.com/questions/6728208/gcc-wont-include-libcurl-on-commandline-for-os-x)
* Etc
  * [curl_easy_setopt - set options for a curl easy handle](https://curl.haxx.se/libcurl/c/curl_easy_setopt.html)
  * [CURLOPT_WRITEFUNCTION explained](https://curl.haxx.se/libcurl/c/CURLOPT_WRITEFUNCTION.html)
  * [CURLOPT_NOSIGNAL explained](https://curl.haxx.se/libcurl/c/CURLOPT_NOSIGNAL.html)
* Troubleshooting
  * CURLE_OPERATION_TIMEDOUT, 28
    * [CURLOPT_TIMEOUT explained](https://curl.haxx.se/libcurl/c/CURLOPT_TIMEOUT.html)
    * [Re: CURL problems detected: 28 => connect() timed out!](https://www.zen-cart.com/showthread.php?128859-CURL-problems-detected-28-gt-connect()-timed-out!)
