# JNI

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
