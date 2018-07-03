from multiprocessing import Manager
from multiprocessing import Process
from multiprocessing import current_process
import logging
import random
import sys
import time


def foo(d, main_num, _id):
    #   Separate logging using FileHandler
    #   Each process logs it's own log in the file 'logs/<process name>.log'
    def get_logger():
        name = current_process().name
        h = logging.FileHandler('logs/{}.log'.format(name))
        FORMAT = "%(asctime)s [%(levelname)s][%(filename)s:%(lineno)s - %(funcName)20s()] %(message)s"
        h.setFormatter(logging.Formatter(FORMAT))
        logger = logging.getLogger(name)
        logger.addHandler(h)
        logger.setLevel(logging.DEBUG)
        return logger

    logger = get_logger()
    rand_num = random.randint(0, 10)
    logger.debug('process [{}] [{}] start sleeping {}...\td = {}'.format(main_num, _id, rand_num, d))
    time.sleep(rand_num)
    logger.debug('process [{}] [{}] end sleeping {}...'.format(main_num, _id, rand_num))
    #   del _id in d to make _id executable again
    del d[_id]


with Manager() as manager:
    d = manager.dict()
    main_cnt = 0
    while True:
        for _id in range(5):
            #   execute process if _id does NOT exist in d
            if _id not in d:
                d[_id] = 'ING by {}'.format(main_cnt)
                p = Process(target=foo, args=(d, main_cnt, _id,))
                p.daemon = True
                p.start()
            else:
                print("main [{}] cannot execute process [{}] because it's working".format(main_cnt, _id))
        time.sleep(4)
        main_cnt += 1
