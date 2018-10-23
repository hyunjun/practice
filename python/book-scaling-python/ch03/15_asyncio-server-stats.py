import asyncio
import time


'''
$ python3 15_asyncio-server-stats.py

$ python3 14_asyncio-tcp-client.py& #   5 times
$ ps -ef | grep 14_
  502 16964 16016   0  2:06PM ttys018    0:04.08 python3 14_asyncio-tcp-client.py
  502 17001 16016   0  2:06PM ttys018    0:03.45 python3 14_asyncio-tcp-client.py
  502 17035 16016   0  2:06PM ttys018    0:03.00 python3 14_asyncio-tcp-client.py
  502 17072 16016   0  2:06PM ttys018    0:02.63 python3 14_asyncio-tcp-client.py
  502 17101 16016   0  2:06PM ttys018    0:02.34 python3 14_asyncio-tcp-client.py
  502 17136 16016   0  2:06PM ttys018    0:00.00 grep --color=auto --exclude-dir=.bzr --exclude-dir=CVS --exclude-dir=.git --exclude-dir=.hg --exclude-dir=.svn 14_
$ kill 16964 17001 17035 17072 17101
[5]  + 17101 terminated  python3 14_asyncio-tcp-client.py
[4]  + 17072 terminated  python3 14_asyncio-tcp-client.py
[3]  + 17035 terminated  python3 14_asyncio-tcp-client.py
[2]  + 17001 terminated  python3 14_asyncio-tcp-client.py
[1]  + 16964 terminated  python3 14_asyncio-tcp-client.py

$ python3 15_asyncio-server-stats.py
^CServer ran for: 21.80 seconds
Connections: 5
Messages sent: 670122
Messages sent per second: 30740.40
'''


SERVER_ADDRESS = ('127.0.0.1', 1234)


class YellEchoServer(asyncio.Protocol):
    def __init__(self, stats):
        self.stats = stats
        self.stats['started at'] = time.time()

    def connection_made(self, transport):
        self.transport = transport
        self.stats['connections'] += 1

    def data_received(self, data):
        self.transport.write(data.upper())
        self.stats['messages sent'] += 1


event_loop = asyncio.get_event_loop()


stats = {
    'started at': time.time(),
    'connections': 0,
    'messages sent': 0,
}


factory = event_loop.create_server(lambda: YellEchoServer(stats), *SERVER_ADDRESS)
server = event_loop.run_until_complete(factory)


try:
    event_loop.run_forever()
except KeyboardInterrupt:
    pass
finally:
    server.close()
    event_loop.run_until_complete(server.wait_closed())
    event_loop.close()

    ran_for = time.time() - stats['started at']
    print('Server ran for: %.2f seconds' % ran_for)
    print('Connections: {}'.format(stats['connections']))
    print('Messages sent: {}'.format(stats['messages sent']))
    print('Messages sent per second: %.2f' % (stats['messages sent'] / ran_for))
