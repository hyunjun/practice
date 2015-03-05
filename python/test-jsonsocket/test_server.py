#-*- coding: utf8 -*-
from jsonsocket import Server
import base64
import json

server = Server('localhost', 49945)
server.accept()
data = server.recv()
#print type(data), data
for k, v in data.items():
  nl = []
  for i in v:
    if isinstance(i, int):
      nl.append(str(i) + '한글화')
    elif isinstance(i, unicode):
      nl.append(i.encode('utf8') + '한글화')
  data[k] = nl
print data
#server.send({'data': base64.decodestring(data)}).close()
server.send({'data': data}).close()
