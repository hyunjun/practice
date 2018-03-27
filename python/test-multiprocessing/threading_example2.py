#   http://sebastiandahlgren.se/2014/06/27/running-a-method-as-a-background-thread-in-python/
from queue import Queue
import threading
import time


class ThreadingExample(object):
    """ Threading example class
    The run() method will be started and it will run in the background
    until the application exits.
    """

    def __init__(self, num, queue, interval=1):
        """ Constructor
        :type interval: int
        :param interval: Check interval, in seconds
        """
        self.num = num
        self.queue = queue
        self.interval = interval

        #   check id of self.queue to know all the threads have the same queue
        print('[{}] {}'.format(self.num, id(self.queue)))

        thread = threading.Thread(target=self.run, args=())
        thread.daemon = True                            # Daemonize thread
        thread.start()                                  # Start the execution

    def run(self):
        """ Method that runs forever """
        while True:
            # Do something
            if self.queue.empty():
                print('[{}] Doing something imporant in the background'.format(self.num))
            else:
                val = self.queue.get()
                print('[{}] Getting {} to do something imporant in the background'.format(self.num, val))

            time.sleep(self.interval)


#   https://docs.python.org/3/library/queue.html
#   queue is thread safe
q = Queue()
examples = [ThreadingExample(0, q), ThreadingExample(1, q)]
q.put(1)
for i in range(3):
    q.put(i * 10)
time.sleep(3)
q.put(100)
print('Checkpoint')
time.sleep(2)
print('Bye')
