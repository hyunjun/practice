ccall
=====
* ref; https://www.reddit.com/r/Julia/comments/3sixgm/need_help_need_to_call_c_functions/
* works on julia version 0.4.5, OSX

  ```
  $ julia -v
  julia version 0.4.5
  $ make build
  gcc -c rosetta.c -o rosetta.o --std=c11 -Wall -fpic
  gcc -dynamiclib rosetta.o -o rosetta.dylib
  $ julia rosetta.jl
  hello_c(5) = (5,"Hello")
  hello_c(13) = (13,"Hello World!")
  hello_c(20) = (13,"Hello World!")
  ```
