import random


import tenacity


def do_something():
    if random.randint(0, 1) == 0:
        print('Failure')
        raise RuntimeError
    print('Success')
    return True


@tenacity.retry(wait=tenacity.wait_fixed(1),
                stop=tenacity.stop_after_delay(60),
                retry=(tenacity.retry_if_exception_type(RuntimeError) |
                       tenacity.retry_if_result(lambda result: result is None)))
def do_something_and_retry():
    do_something()


do_something_and_retry()
