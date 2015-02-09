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
def countdown(n):
    """
    Counts down
    :param n:
    :return:
    """
    while n > 0:
        n -= 1

countdown(1000000)
# countdown 0.13044190406799316
countdown(3000000)
# countdown 0.36681318283081055
print(countdown.__doc__)   # 带上@wrap才有这个
    # Counts down
    # :param n:
    # :return:
    #
countdown.__wrapped__(10000)