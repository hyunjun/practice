import threading
import time


import cotyledon


#   pip install cotyledon
#   https://cotyledon.readthedocs.io/en/latest/api.html


class PrinterService(cotyledon.Service):
    name = 'printer'

    def __init__(self, worker_id):
        super(PrinterService, self).__init__(worker_id)
        self._shutdown = threading.Event()

    def run(self):
        while not self._shutdown.is_set():
            print('Doing stuff')
            time.sleep(1)

    def terminate(self):
        self._shutdown.set()


manager = cotyledon.ServiceManager()
# cotyledon will run 2 processes
manager.add(PrinterService, 2)
manager.run()
