import random
import threading
import time


#   https://stackoverflow.com/questions/16199793/simple-threading-event-example


def foo(i):
    time.sleep(random.random() * i)
    if i == 5:
        print('raise Exception at {}'.format(i))
        raise Exception
    print('Exit thread {}'.format(i))


if __name__ == '__main__':
    for i in range(10):
        t = threading.Thread(target=foo, args=(i,))
        #t.daemon = True
        t.start()
    time.sleep(1)
    print('end of main')
