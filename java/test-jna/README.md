# test-jna
* ref
  * [loading-a-custom-library-with-jna-on-windows](http://stackoverflow.com/questions/30327006/loading-a-custom-library-with-jna-on-windows)
  * [JAVA native access examples](http://jnaexamples.blogspot.com/2012/03/java-native-access-is-easy-way-to.html)
* compile & execution
  * [jna-4.2.2.jar](https://maven.java.net/content/repositories/releases/net/java/dev/jna/jna/4.2.2/jna-4.2.2.jar) from [jna](https://github.com/java-native-access/jna)
  * compile C

    ```
    # Redhat 6.6
    $ gcc -c -Wall -Werror -fPIC test.c
    $ gcc -shared -o ./lib/libtest.so test.o

    # OS X
    $ gcc -I/System/Library/Frameworks/JavaVM.framework/Versions/A/Headers -o ./lib/libtest.dylib -shared test.c
    ```
  * compile java & execution

    ```
    $ javac -cp ./lib/jna-4.2.2.jar:. MyStruct.java StringByReference.java
    $ jar cvf ./lib/mylib.jar MyStruct.class StringByReference.class
    $ \rm *.class *.o

    $ javac -cp ./lib/jna-4.2.2.jar:./lib/mylib.jar:. TestJNA.java

    $ java -cp .:./lib/jna-4.2.2.jar:./lib/mylib.jar -Djna.library.path=./lib/ TestJNA
    getpid()        12703
    getppid()       683
    time()  1479954286
    ImAString
    11
    7
    4
    5
    5.3
    Native allocted pointer  0x7ff39dc2dcb0
    Struct field has values 10000 20099
    Java got from  native 140684300573872  10000 20099
    Native Freeing mem 0x7ff39dc2dcb0 with val 10000 20099
    Native recived string ZZZZZ
    1ZZZZ
    Native will set first char to 1 in that stringNative recieved the pointer to an
    array of structures with 10 elements
    Struct no 0 values 0 100
    Struct no 1 values 1 101
    Struct no 2 values 2 102
    Struct no 3 values 3 103
    Struct no 4 values 4 104
    Struct no 5 values 5 105
    Struct no 6 values 6 106
    Struct no 7 values 7 107
    Struct no 8 values 8 108
    Struct no 9 values 9 109
    ```
