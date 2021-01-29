from multiprocessing import Process, Semaphore, shared_memory
import multiprocessing
import numpy as np
import time


#   https://github.com/cadop/dijkstra/blob/4535350df267341925dace0224558e3cc8a2028c/code/dijkstra_shm.py
def shared_to_numpy(shared_arr, dtype, shape):
    return np.frombuffer(shared_arr, dtype=dtype).reshape(shape)


def create_shared_array(dtype, shape):
    dtype = np.dtype(dtype)
    cdtype = np.ctypeslib.as_ctypes_type(dtype)
    shared_arr = multiprocessing.RawArray(cdtype, sum(shape))
    arr = shared_to_numpy(shared_arr, dtype, shape)
    return shared_arr, arr


class Reader(Process):

    def __init__(self, sharedArr):
        Process.__init__(self)

        self.sharedArr = sharedArr
        print('Reader init:', *self.sharedArr)
        time.sleep(2)

    def run(self):            
        print('Reader run 0:', *self.sharedArr)
        time.sleep(2)
        print('Reader run 1:', *self.sharedArr)
        time.sleep(1)


class Worker(Process):

    def __init__(self, sharedArr):
        Process.__init__(self)

        self.sharedArr = sharedArr
        print('Worker init:', *self.sharedArr)
        time.sleep(2)

    def run(self):            
        print('Worker run 0:', *self.sharedArr)
        self.sharedArr[-1] = 9
        print('Worker run 1:', *self.sharedArr)
        time.sleep(1)


if __name__ == "__main__":
    multiprocessing.freeze_support()

    a = np.array([1, 1, 2, 3, 5, 8])
    shared_arr, arr = create_shared_array(a.dtype, a.shape)
    shared_arr[:] = a[:]
    print('main:', *shared_arr)


    th1 = Reader(shared_arr)
    th2 = Worker(shared_arr)

    th1.start()
    th2.start()

    th2.join()
    th1.join()

    time.sleep(3)
    print('main:', *shared_arr)
    time.sleep(3)
