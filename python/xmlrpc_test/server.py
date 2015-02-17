#-*- coding: utf8 -*-
from SimpleXMLRPCServer import SimpleXMLRPCServer, SimpleXMLRPCRequestHandler
import base64

class TestWrapper(object):
  def __init__(self):
    pass

  def do_something(self, inp):
    return inp.split()

  def analyze(self, inp):
    return self.do_something(base64.decodestring(inp))

def service():
  test_wrapper = TestWrapper()
  from SocketServer import ThreadingMixIn
  class SimpleThreadXMLRPCServer(ThreadingMixIn, SimpleXMLRPCServer):
    pass
  class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/xmlrpc_test')
  server = SimpleThreadXMLRPCServer(('0.0.0.0', 49944),
                                    requestHandler=RequestHandler,
                                    logRequests=False,
                                    allow_none=True,
                                   )
  server.register_introspection_functions()
  server.register_instance(test_wrapper)
  server.serve_forever()

if __name__=='__main__':
  service()
