import time
from functools import wraps

def timethis(func):
    @wraps(func)   ## 一定要带上这个！！
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(func.__name__, end-start)
        return result
    return wrapper

@timethis
def add(x, y):
    return x + y

z = add(1, 2)
print(z)
# add 1.9073486328125e-06
# 3

# 调用不带装饰器的add
orig_add = add.__wrapped__
z = orig_add(2, 3)
print(z)
# 5