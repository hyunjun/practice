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

queues = {0: Queue(), 1: Queue()}
examples = [ThreadingExample(0, queues[0]), ThreadingExample(1, queues[1])]
queues[0].put(1)
for i in range(3):
    queues[1].put(i * 10)
time.sleep(3)
queues[1].put(100)
print('Checkpoint')
time.sleep(2)
print('Bye')
