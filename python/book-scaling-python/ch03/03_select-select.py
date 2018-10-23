import select
import socket


s = socket.create_connection(('httpbin.org', 80))
s.setblocking(False)
s.send(b'GET /delay/1 HTTP/1.1\r\nHost: httpbin.org\r\n\r\n')
while True:
    ready_to_read, ready_to_write, in_error = select.select([s], [], [])
    if s in ready_to_read:
        buf = s.recv(1024)
        print(buf)
        break
