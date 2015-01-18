# > time python sample.py
# > python -m cProfile sample.py

import time
from functools import wraps


"""
记录某个函数的运行时间
"""
# 1. 装饰器
def timethis(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        r = func(*args, **kwargs)
        end = time.perf_counter()
        print('{}.{}:{}'.format(func.__module__, func.__name__, end-start))
        return r
    return wrapper

@timethis
def countdown(n):
    while n > 0:
        n -= 1

countdown(100000)
# __main__.countdown:0.0124830020013178

# 2. contextmanaget的形式
from contextlib import contextmanager
@contextmanager
def timeblock(label):
    start = time.perf_counter()
    try:
        yield
    finally:
        end = time.perf_counter()
        print('{}:{}'.format(label, end-start))

with timeblock('counting'):
    n = 100000
    while n > 0:
        n -= 1

# counting:0.020528508997813333

# 3. timeit --> 小代码片段, number可以指定运行次数
from timeit import timeit
print(timeit('math.sqrt(2)', 'import math'))
print(timeit('sqrt(2)', 'from math import sqrt', number=1000))
# 0.17827510399729363
# 0.13633526900230208