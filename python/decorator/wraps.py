'''
Python Essential Reference p332
'''
from functools import wraps

def debug(func):
    @wraps(func)
    def wrapped(*args, **kwargs):
        print("Calling %s" % func.__name__)
        r = func(*args, **kwargs)
        print("Done calling %s" % func.__name__)
    return wrapped

@debug
def add(x, y):
    return x + y
