import random


import tenacity


def do_something():
    if random.randint(0, 1) == 0:
        print('Failure')
        raise RuntimeError
    print('Success')


@tenacity.retry(wait=tenacity.wait_fixed(10) + tenacity.wait_random(0, 3))
def do_something_and_retry():
    do_something()


do_something_and_retry()
