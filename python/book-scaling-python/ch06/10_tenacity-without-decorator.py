import random


import tenacity


def do_something():
    if random.randint(0, 1) == 0:
        print('Failure')
        raise IOError
    print('Success')
    return True


r = tenacity.Retrying(
    wait=tenacity.wait_fixed(1),
    retry=tenacity.retry_if_exception_type(IOError))
r.call(do_something)
