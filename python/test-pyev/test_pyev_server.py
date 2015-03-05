#!/daum/program/anaconda/bin/python
#-*- coding: utf8 -*-
import pyev
import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setblocking(0)

server.bind(('localhost', 49944))
server.listen(8)
def server_activity(watcher, revents):
  connection, client_address = server.accept()
  data = connection.recv(256)
  #connection.send("hello\n")
  connection.send(data + ' received \n')
  connection.close()

loop = pyev.default_loop()
watcher = pyev.Io(server, pyev.EV_READ, loop, server_activity)
watcher.start()
loop.start()
