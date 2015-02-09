* execution `$ streaming.sh`
  * test 환경
    * CDH5.3 (Hadoop 2.5.0-cdh5.3.0 / Pig version 0.12.0-cdh5.3.0)
    * CDH4.5 (Hadoop 2.0.0-cdh4.5.0 / Pig version 0.11.0-cdh4.5.0)
* files
  * mapper*.py; map 동작을 위한 python script
    * mapper1.py; system default가 아닌 별도 설치 python을 설치하는 경우
  * external.py; mapper가 참조하는 외부 python script
  * streaming.pig; pig 실행 script
  * streaming.sh; hadoop streaming과 pig를 차례로 실행시키는 test script
  * test_data; 간단한 test용 data
    * test_data_160_194는 utf8 160, 194 값이 있는데 일반적인 whitespace가 아니라 처리 방법을 아직 정확히 모르겠음
* 주의점
  * python 환경을 전부 동일하게
    * 예를 들어 `#!/usr/bin/env python`으로 하면 system default python을 사용
    * anaconda라면 `#!/anaconda/installed/directory/bin/python`으로 수정
  * python script를 단독으로 실행(ex. `$ ./mapper.py < test_data`)시 무조건 오류가 없어야 함
    * 오류가 없다고 무조건 streaming이 되는 건 아니지만, 오류가 있으면 무조건 실패
    * pig가 hadoop streaming보다 python 오류에 취약함
      * mapper.py는 hadoop streaming/pig 모두 동작
      * mapper2.py는 hadoop streaming만 정상 동작
    * 하지만 directory에 어떤 resource가 있고 해당 directory를 사용하는 경우 hadoop streaming은 안 되지만, pig는 되는 걸로 보임(아직 정확하진 않음)
  * pig에 ship하는 file들은 full path 사용, directory는 ship할 수 없으므로 모든 클러스터에 동일하게 설치
  * `failed with exit status: 1`
    * python2.7이 아닌데 print에서 기존의 %s가 아니라 str.format을 사용하는 경우
    * 호출하려고 import한 python file(아래 예제의 external.py)이
      * streaming의 -files나 pig의 SHIP에 기술되지 않고
      * sys.path.append('.')로 추가 python file을 참조할 위치를 지정하지 않은 경우
    * 별도 library 사용시 모든 클러스터에 동일하게 library 설치 필요 (ex. `import networkx`)
* [ref](http://www.michael-noll.com/tutorials/writing-an-hadoop-mapreduce-program-in-python/)
