def add(a, b):
    return a + b


def mult(a, b):
    return a * b


import time


class Calculator:
    def sum(self, a, b):
        time.sleep(10)
        return a + b


import redis


class TestRedis:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.connect()

    def connect(self):
        try:
            self.conn = redis.StrictRedis(host=self.host, port=self.port, db=0)
        except redis.exceptions.ConnectionError as e:
            print('Exception at conn {}'.format(e))

    def info(self):
        return self.conn.info()

    def echo(self, msg):
        return self.conn.echo(msg)


if __name__ == '__main__':
    testRedis = TestRedis('127.0.0.1', 6379)
    print(testRedis.info())
    print(testRedis.echo('test'))
