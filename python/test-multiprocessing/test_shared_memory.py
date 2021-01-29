from multiprocessing import Process, Semaphore, shared_memory
import numpy as np
import time


#   https://docs.python.org/ko/3.10/library/multiprocessing.shared_memory.html
class Reader(Process):

    def __init__(self, a, shmName):
        Process.__init__(self)

        self.shm = shared_memory.SharedMemory(name=shmName)
        self.b = np.ndarray(a.shape, dtype=a.dtype, buffer=self.shm.buf) 
        print('Reader init. name:', self.shm.name, self.b.shape, self.b)
        time.sleep(2)

    def run(self):            
        print('Reader run 0:', self.shm.name, self.b.shape, self.b)
        time.sleep(2)
        print('Reader run 1:', self.shm.name, self.b.shape, self.b)
        time.sleep(1)
        self.shm.close()

class Worker(Process):

    def __init__(self, a, shmName):
        Process.__init__(self)

        self.shm = shared_memory.SharedMemory(name=shmName) 
        self.b = np.ndarray(a.shape, dtype=a.dtype, buffer=self.shm.buf) 
        print('Worker init. name:', self.shm.name, self.b.shape, self.b)
        time.sleep(2)

    def run(self):            
        print('Worker run 0:', self.shm.name, self.b.shape, self.b)
        self.b[-1] = 888    #   This is NOT shared with Reader & main processes. Why?
        print('Worker run 1:', self.shm.name, self.b.shape, self.b)
        time.sleep(1)
        self.shm.close()


if __name__ == "__main__":
    a = np.array([1, 1, 2, 3, 5, 8])
    shm = shared_memory.SharedMemory(create=True, size=a.nbytes) 
    b = np.ndarray(a.shape, dtype=a.dtype, buffer=shm.buf)
    b[:] = a[:]
    print('main name:', b, shm.name, b.shape)

    th1 = Reader(b, shm.name)
    th2 = Worker(b, shm.name)
    b[-1] = 999 #   This is shared with Reader & Worker processes

    th1.start()
    th2.start()

    th2.join()
    th1.join()

    time.sleep(3)
    print('main name:', b, shm.name, b.shape)
    time.sleep(3)
    shm.close()
    shm.unlink()
