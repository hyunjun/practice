#-*- coding: utf8 -*-
from jsonsocket import Client
import base64

client = Client()
#client.connect('localhost', 49945).send({'some_list': [123, 456]})#, base64.encodestring('한글')]})
client.connect('localhost', 49945).send({'some_list': [123, 456, '한글']})
response = client.recv()
for k, v in response['data'].items():
  print k
  for i in v:
    print i
client.close()
