from multiprocessing import Process, Semaphore, shared_memory
import numpy as np
import time


dtype_eV = np.dtype({ 'names':['xCor', 'yCor', 'size'], 'formats':['int32', 'float64', 'float64'] })


def worker_writer(id, a, shm):
    exst_shm = shared_memory.SharedMemory(name=shm)
    b = np.ndarray(a.shape, dtype=a.dtype, buffer=exst_shm.buf)

    for i in range(5):
        b['xCor'][i] = i
        b['yCor'][i] = i
        b['size'][i] = i*10


def worker_reader(id, a, shm):
    exst_shm = shared_memory.SharedMemory(name=shm)
    b = np.ndarray(a.shape, dtype=a.dtype, buffer=exst_shm.buf)

    time.sleep(0.5)
    print(b)


class Wrapper(Process):
    def __init__(self, id, a, shm, func):
        super(Wrapper, self).__init__()
        self.id, self.a, self.shm, self.func = id, a, shm, func
        print(f'Writer {self.a} {self.shm}')

    def run(self):
        self.func(self.id, self.a, self.shm)


if __name__ == "__main__":
    a = np.zeros(5, dtype=dtype_eV)
    shm = shared_memory.SharedMemory(create=True, size=a.nbytes)
    c = np.ndarray(a.shape, dtype=a.dtype, buffer=shm.buf)

    print(f'main {a} {shm}')
    #   class에서 직접 shared memory를 쓰는 건 동작하지 않아(이유를 잘 모르겠음) 이런 식으로 구현
    th1 = Wrapper(1, a, shm.name, worker_writer)
    th2 = Wrapper(2, a, shm.name, worker_reader)

    th1.start()
    th2.start()

    th1.join()
    th2.join()

    shm.close()
    shm.unlink()
