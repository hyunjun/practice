# JNI hello world

  ```
  $ vi HelloWorld.java
  $ javac HelloWorld.java
  $ javah -jni HelloWorld

  $ vi helloworld.c
  # Redhat
  $ gcc -c -Wall -Werror -fpic helloworld.c
  $ gcc -shared -o libhelloworld.so helloworld.o
  # for OS X, find the location which holds jni.h & jni_md.h
  $ gcc -I/System/Library/Frameworks/JavaVM.framework/Versions/A/Headers -o libhelloworld.dylib -shared helloworld.c

  $ java -Djava.library.path=. HelloWorld
  ```
