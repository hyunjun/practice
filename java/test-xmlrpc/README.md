* test
  ```
  $ mvn compile package -DskipTests
  $ python ../../python/xmlrpc_test/server.py
  $ java -cp ./target/test-xmlrpc-1.0-SNAPSHOT-jar-with-dependencies.jar net.jun.practice.App "xmlrpc  테스트"
  ```
* caution
  * 한글 사용을 위해 object를 object array로 바꾸는 등의 작업이 필요한 줄 알았지만, 그냥 Object를 출력하면 됐음
    * http://stackoverflow.com/questions/12913888/python-list-in-java
  * Object <-> byte[]; http://sdw8001.tistory.com/20
  * Object -> Array; http://stackoverflow.com/questions/1611735/java-casting-object-to-array-type
  * String <-> byte[]
    * http://stackoverflow.com/questions/18571223/how-to-convert-java-string-into-byte
    * http://jh-note.blogspot.kr/2013/11/byte-string.html
    * http://wolfwideweb.tistory.com/80
  * 한글 분리; http://dev4u.tistory.com/entry/Java-%ED%95%9C%EA%B8%80%EC%9E%90%EB%A5%B4%EA%B8%B0
  * 유니코드 & 한글; http://helloworld.naver.com/helloworld/textyle/76650
  * 한글 인코딩; http://forum.falinux.com/zbxe/?mid=lecture_tip&comment_srl=518031&page=4&l=vi&document_srl=786533
  * ObjectInputStream; http://stackoverflow.com/questions/16447788/set-header-web-socket
  * ByteArrayInputStream, ByteArrayOutputStream; http://baeksupervisor.tistory.com/39
  * `StreamCorruptedException: invalid stream header...`; http://kugistory.net/42
  * String -> InputStream; http://www.mkyong.com/java/how-to-convert-string-to-inputstream-in-java/
* ref
  * https://ws.apache.org/xmlrpc/client.html
  * http://ws.apache.org/xmlrpc/xmlrpc-dist/dependencies.html
  * http://stackoverflow.com/questions/17561667/please-help-porting-xmlrpc-java-syntax-to-python
  * http://onlinebase64decoder.com/functions.php
  * https://github.com/mcasperson/vaultdemo/blob/master/src/main/java/com/redhat/ecs/App.java
