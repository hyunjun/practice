if __name__ == '__main__':
  languages = 'C:CPP:JAVA:PYTHON:PERL:PHP:RUBY:CSHARP:HASKELL:CLOJURE:BASH:SCALA:ERLANG:CLISP:LUA:BRAINFUCK:JAVASCRIPT:GO:D:OCAML:R:PASCAL:SBCL:DART:GROOVY:OBJECTIVEC'.split(':')
  N = int(raw_input())
  for i in range(N):
    api_id, language = raw_input().split()
    if language in languages:
      print 'VALID'
    else:
      print 'INVALID'
