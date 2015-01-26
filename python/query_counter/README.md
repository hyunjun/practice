# query counter
* 목적; 기간별 query count를 조회
  * 입력 데이터는 각 line이 'query\tcount'인 txt file
  * 입력 시간은 중요하지 않음
  * 빠른 조회가 중요하기 때문에 bianry indexed tree를 사용한다고 가정
* key - query, value - list, init [0] \* 256
* tests
  * query_counter.py
    * redis 2.8.19
      * redis.conf에서 다른 설정은 수정하지 않고 maxmemory만 1281666400로 수정
    * result; memory usage 22G, 32,454,266개까지 입력 가능
      * maxmemory 설정보다 memory를 더 쓰는 건 어떤 의미인가?
      * prefix, suffix 조회 부분에 문제
  * query_counter_shelf.py
    * shelf 이용
    * 약 500만개 데이터에서 조회 2m37.120s 소요
  * query_counter_dict.py
    * python 기본 dictionary 이용
    * 약 500만개 데이터에서 조회 77m23.643s 소요
  * sqlite3도 테스트해보려 했지만, 정상 동작하지 않음
