import multiprocessing
import time


import cotyledon


'''
$ ps ax | grep 20_reconfig-process
21152 pts/5    T      0:00 vim 20_reconfig-process.py
22845 pts/5    Sl+    0:00 20_reconfig-process.py: master process [20_reconfig-process.py]
22847 pts/5    Sl+    0:00 20_reconfig-process.py: master process [20_reconfig-process.py]
22853 pts/5    Sl+    0:00 20_reconfig-process.py: ProducerService worker(0)
22858 pts/5    Sl+    0:00 20_reconfig-process.py: printer worker(0)
22863 pts/5    Sl+    0:00 20_reconfig-process.py: printer worker(1)
23764 pts/12   S+     0:00 grep --color=auto 20_reconfig-process
$ kill -HUP 22845 # this SIGHUP(signal hang up) will call Manager.reload and make PrinterService five
'''


class Manager(cotyledon.ServiceManager):
    def __init__(self):
        super(Manager, self).__init__()
        queue = multiprocessing.Manager().Queue()
        self.add(ProducerService, args=(queue,))
        self.printer = self.add(PrinterService, args=(queue,), workers=2)
        self.register_hooks(on_reload=self.reload)

    def reload(self):
        print('Reloading')
        self.reconfigure(self.printer, 5)


class ProducerService(cotyledon.Service):
    def __init__(self, worker_id, queue):
        super(ProducerService, self).__init__(worker_id)
        self.queue = queue

    def run(self):
        i = 0
        while True:
            self.queue.put(i)
            i += 1
            time.sleep(1)


class PrinterService(cotyledon.Service):
    name = 'printer'

    def __init__(self, worker_id, queue):
        super(PrinterService, self).__init__(worker_id)
        self.queue = queue

    def run(self):
        while True:
            job = self.queue.get(block=True)
            print('I am woker: {} PID: {} and I print {}'.format(self.worker_id, self.pid, job))


Manager().run()
