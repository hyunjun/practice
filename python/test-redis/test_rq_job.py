from redis import Redis
from rq import Queue
import time


def my_work(arr):
    return sum(arr)


if __name__ == '__main__':
    queues = [Queue('even', connection=Redis('127.0.0.1', 56379)), Queue('odd', connection=Redis('127.0.0.1', 56379))]
    print('q len {}'.format(len(queues)))
    #job = q.enqueue(my_work, [1, 2, 3, 4, 5])
    # simple queue with redis backend
    # http://python-rq.org/docs/
    # https://github.com/rq/rq/blob/master/rq/job.py
    jobs = []
    for i in range(5, 7):
        if i % 2 == 0:
            jobs.append(queues[0].enqueue_call(func=my_work, args=(list(range(i)),)))
        else:
            jobs.append(queues[1].enqueue_call(func=my_work, args=(list(range(i)),)))
    #print(q.job_ids)
    #print(q.jobs)
    for job in jobs:
        print(job)
        while job.get_status() == 'queued':
            time.sleep(0.1)
        print(job.result)
    queues[0].delete(delete_jobs=True)
    queues[1].delete(delete_jobs=True)
