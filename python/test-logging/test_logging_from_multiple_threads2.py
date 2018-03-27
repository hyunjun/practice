import logging
import logging.handlers
import threading
import time


class ThreadingExample:

    def __init__(self, logger, num, info, interval=1):
        self.logger = logger
        self.num = num
        self.info = info
        self.interval = interval

        time.sleep(self.interval * 0.1)

        self.thread = threading.Thread(target=self.run, args=())
        self.thread.daemon = True
        self.thread.start()

    def run(self):
        while not self.info['stop']:
            self.logger.debug('[{}] Hi from myfunc'.format(self.num))
            time.sleep(self.interval)


def main():
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    ch = logging.handlers.TimedRotatingFileHandler('logs/multithread.log', when="midnight", interval=1, backupCount=100)
    ch.setFormatter(logging.Formatter('%(relativeCreated)6d %(threadName)s %(message)s'))
    logger.addHandler(ch)

    NUM_THREADS, info = 2, {'stop': False}

    examples = [ThreadingExample(logger, i, info) for i in range(NUM_THREADS)]
    while True:
        try:
            logging.debug('Hello from main')
            time.sleep(0.75)
        except KeyboardInterrupt:
            info['stop'] = True
            break


if __name__ == '__main__':
    main()
