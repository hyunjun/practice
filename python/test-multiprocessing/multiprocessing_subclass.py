#   https://pymotw.com/3/multiprocessing/basics.html
import multiprocessing
import os


class Worker(multiprocessing.Process):

    def run(self):
        print(f'{os.getpid()} In {self.name}')
        return


if __name__ == '__main__':
    jobs = []
    for i in range(5):
        p = Worker()
        jobs.append(p)
        p.start()
    for j in jobs:
        j.join()
