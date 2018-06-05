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


import requests


class TestAPI:
    def __init__(self, host, port):
        self.host = host
        self.port = port

    def call(self):
        url = '{}:{}'.format(self.host, self.port)
        r = None
        try:
            print('requests url {}'.format(url))
            r = requests.get(url)
            print('\trequested url {}'.format(r.url))
        except requests.exceptions.ConnectionError:
            print('requests.exceptions.ConnectionError from'.format(url))
            return {}

        if r is None or r.status_code != 200:
            print('Error from {}'.format(url))
            return {}

        return r.json()


if __name__ == '__main__':
    testRedis = TestRedis('127.0.0.1', 6379)
    print(testRedis.info())
    print(testRedis.echo('test'))
