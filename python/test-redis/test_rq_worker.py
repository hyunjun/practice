from redis import Redis
from rq import Connection, Queue, Worker


def my_work(arr):
    return sum(arr)


if __name__ == '__main__':
    with Connection(Redis('127.0.0.1', 56379)):
        queues = [Queue('odd'), Queue('even')]
        Worker(queues).work()
