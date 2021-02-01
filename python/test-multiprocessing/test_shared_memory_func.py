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


if __name__ == "__main__":
    a = np.zeros(5, dtype=dtype_eV)
    shm = shared_memory.SharedMemory(create=True, size=a.nbytes)
    c = np.ndarray(a.shape, dtype=a.dtype, buffer=shm.buf)
    th1 = Process(target=worker_writer, args=(1, a, shm.name))
    th2 = Process(target=worker_reader, args=(2, a, shm.name))

    th1.start()
    th2.start()
    th1.join()
    th2.join()

    shm.close()
    shm.unlink()
