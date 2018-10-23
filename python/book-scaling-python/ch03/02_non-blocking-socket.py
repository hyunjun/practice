import socket


s = socket.create_connection(('httpbin.org', 80))
s.setblocking(False)
s.send(b'GET /delay/5 HTTP/1.1\r\nHost: httpbin.org\r\n\r\n')
buf = s.recv(1024)
print(buf)
