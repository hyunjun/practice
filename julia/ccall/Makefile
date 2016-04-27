rosetta.o: rosetta.c
	gcc -c rosetta.c -o rosetta.o -Wall -fpic

rosetta.so: rosetta.o
	gcc -shared -o rosetta.so rosetta.o

clean:
	-rm *.o *.so
