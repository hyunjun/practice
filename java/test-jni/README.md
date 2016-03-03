# JNI
* reference
  * [Java Native Interface (JNI)](https://www3.ntu.edu.sg/home/ehchua/programming/java/JavaNativeInterface.html)
  * [[JNI] String Array 관리](http://gogorchg.tistory.com/entry/JNI-String-Array-%EA%B4%80%EB%A6%AC)
  * [JNI ( JAVA NATIVE INTERFACE ) FOR C/C++ WITH EXAMPLES](https://chandruscm.wordpress.com/tag/how-to-pass-string-array-from-c-to-java/)
  * [Working With Java Arrays in Native Methods](http://www.math.uni-hamburg.de/doc/java/tutorial/native1.1/implementing/array.html)
  * [JNI Part1: Java Native Interface Introduction and “Hello World” application](http://electrofriends.com/articles/jni/jni-part1-java-native-interface/)
  * [간단한 Java Native Interface 예제](http://www.hanbit.co.kr/network/view.html?bi_id=1033)
  * [Why am I getting this UnsatisfiedLinkError with native code?](http://stackoverflow.com/questions/761639/why-am-i-getting-this-unsatisfiedlinkerror-with-native-code)
  * [How to use a jobject array ? (Jni)](http://stackoverflow.com/questions/8079976/how-to-use-a-jobject-array-jni)
  * [passing string array from java to C with JNI](http://stackoverflow.com/questions/5972207/passing-string-array-from-java-to-c-with-jni)
* hello world

  ```
  $ vi HelloWorld.java
  $ javac HelloWorld.java
  $ javah -jni HelloWorld

  $ vi helloworld.c
  # Redhat
  $ gcc -c -Wall -Werror -fpic helloworld.c
  # -I if "fatal error: jni[_md].h: No such file or directory" occurs
  # gcc -c -I[jni.h directory] -I[jni_md.h directory] -Wall -Werror -fpic helloworld.c
  # i.e. gcc -c -I/usr/java/jdk1.8.0_25/include -I/usr/java/jdk1.8.0_25/include/linux -Wall -Werror -fpic helloworld.c
  $ gcc -shared -o libhelloworld.so helloworld.o
  # for OS X, find the location which holds jni.h & jni_md.h
  $ gcc -I/System/Library/Frameworks/JavaVM.framework/Versions/A/Headers -o libhelloworld.dylib -shared helloworld.c

  $ java -Djava.library.path=. HelloWorld
  ```
