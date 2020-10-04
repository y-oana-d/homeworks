import datetime
from functools import wraps
from time import time


def time_elapsed(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        start = datetime.datetime.now()
        result = f(*args, **kwargs)
        end = datetime.datetime.now()
        print(f'The execution started at {start}')
        print(f'The execution ended at {end}')
        print(f'Time elapsed on this execution is {end-start}')
        return result
    return wrapper

@time_elapsed
def f(a):
    for i in range(a):
        pass
print(f(2000000))





