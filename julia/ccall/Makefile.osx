rosetta.o: rosetta.c
	gcc -c rosetta.c -o rosetta.o --std=c11 -Wall -fpic

rosetta.dylib: rosetta.o
	gcc -dynamiclib rosetta.o -o rosetta.dylib

build: rosetta.dylib

clean:
	-rm *.o
	-rm *.dylib
