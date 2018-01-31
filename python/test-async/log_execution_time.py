from functools import wraps
from time import time


def log_execution_time(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time()
        return_value = func(*args, **kwargs)
        message = 'Executing {} took {:.03} seconds.'.format(func.__name__, time() - start)
        print(message)
        return return_value
    return wrapper
