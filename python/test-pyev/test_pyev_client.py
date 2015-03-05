#!/daum/program/anaconda/bin/python
#-*- coding: utf8 -*-
import base64
import socket
import sys

if __name__ == '__main__':
  if len(sys.argv) < 2:
    sys.exit(1)
  #proxy = xmlrpclib.ServerProxy("http://10.15.86.206:49944/dha")
  #for t in proxy.analyze(base64.encodestring(sys.argv[1])):
  #  print t
  s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  s.connect(('localhost', 49944))
  s.send(sys.argv[1])
  print s.recv(256)
