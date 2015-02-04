* execution `$ streaming.sh`
  * test 환경
    * CDH5.3 (Hadoop 2.5.0-cdh5.3.0 / Pig version 0.12.0-cdh5.3.0)
    * CDH4.5 (Hadoop 2.0.0-cdh4.5.0 / Pig version 0.11.0-cdh4.5.0)
* files
  * mapper.py, mapper2.py; map 동작을 위한 python script
  * external.py; mapper가 참조하는 외부 python script
  * streaming.pig; pig 실행 script
  * streaming.sh; hadoop streaming과 pig를 차례로 실행시키는 test script
  * test_data; 간단한 test용 data
    * test_data_160_194는 utf8 160, 194 값이 있는데 일반적인 whitespace가 아니라 처리 방법을 아직 정확히 모르겠음
* 주의점
  * python script를 단독으로 실행(ex. `$ ./mapper.py < test_data`)시 무조건 오류가 없어야 함
    * 오류가 없다고 무조건 streaming이 되는 건 아니지만, 오류가 있으면 무조건 실패
    * pig가 hadoop streaming보다 python 오류에 취약함
      * mapper.py는 hadoop streaming/pig 모두 동작
      * mapper2.py는 hadoop streaming만 정상 동작
  * `failed with exit status: 1`
    * print에서 기존의 %s가 아니라 str.format을 사용하는 경우
    * 호출하려고 import한 python file(아래 예제의 external.py)이
      * streaming의 -files나 pig의 SHIP에 기술되지 않고
      * sys.path.append('.')로 추가 python file을 참조할 위치를 지정하지 않은 경우
    * 라이브러리를 참조하는 경우(미해결)
* [ref](http://www.michael-noll.com/tutorials/writing-an-hadoop-mapreduce-program-in-python/)
