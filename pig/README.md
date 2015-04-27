Pig
===
* diff
  * diff2.pig
    * [A Simple Explanation of COGROUP in Apache Pig](http://joshualande.com/cogroup-in-pig/)
    * 28억행(2877773812 line), 112GB(119496321285 byte) file 비교에 약 1h 52m 소요
    * 실행 전 `sync; echo 3 > /proc/sys/vm/drop_caches`로 memory 확보함
    * pig version 0.12.0-cdh5.2.0
    * server cpu Intel(R) Xeon(R) CPU E5-2430 0 @ 2.20GHz * 24, memory 49535824 kB
  * diff1.pig
    * 같은 server인데도 diff2.pig와 달리 실패한 요인은 다음 두 가지로 추정
    * memory를 적게 할당
    * 양쪽 file의 결과를 전부 쓰게 코드 작성
