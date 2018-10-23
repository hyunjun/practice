import random


import tenacity


def do_something():
    if random.randint(0, 1) == 0:
        print('Failure')
        raise RuntimeError
    print('Success')


@tenacity.retry(wait=tenacity.wait_fixed(1), retry=tenacity.retry_if_exception_type(RuntimeError))
def do_something_and_retry():
    do_something()


do_something_and_retry()
