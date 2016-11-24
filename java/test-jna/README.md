# test-jna
* [loading-a-custom-library-with-jna-on-windows](http://stackoverflow.com/questions/30327006/loading-a-custom-library-with-jna-on-windows)
* compile & execution
  * [jna-4.2.2.jar](https://maven.java.net/content/repositories/releases/net/java/dev/jna/jna/4.2.2/jna-4.2.2.jar) from [jna](https://github.com/java-native-access/jna)
  * compile C

    ```
    # Redhat 6.6
    $ gcc -c -Wall -Werror -fPIC test.c
    $ gcc -shared -o libtest.so test.o

    # OS X
    $ gcc -I/System/Library/Frameworks/JavaVM.framework/Versions/A/Headers -o libtest.dylib -shared test.c
    ```
  * compile java & execution

    ```
    $ javac -cp ./jna-4.2.2.jar:. TestJNA.java

    $ java -cp .:jna-4.2.2.jar -Djava.library.path=. TestJNA
    ImAString
    ```
