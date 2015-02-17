#-*- coding: utf8 -*-
import base64
import sys
import xmlrpclib

if __name__ == '__main__':
  if len(sys.argv) < 2:
    sys.exit(1)
  proxy = xmlrpclib.ServerProxy("http://localhost:49944/xmlrpc_test")
  for t in proxy.analyze(base64.encodestring(sys.argv[1])):
    print t
