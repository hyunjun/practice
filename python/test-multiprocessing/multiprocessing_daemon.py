from multiprocessing import Manager
from multiprocessing import Process
import random
import sys
import time


def foo(d, main_num, _id):
    rand_num = random.randint(0, 10)
    print('process [{}] [{}] start sleeping {}...\td = {}'.format(main_num, _id, rand_num, d))
    time.sleep(rand_num)
    print('process [{}] [{}] end sleeping {}...'.format(main_num, _id, rand_num))
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
