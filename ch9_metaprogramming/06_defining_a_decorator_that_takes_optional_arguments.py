import logging
from functools import wraps, partial

def logged(func=None, *, level=logging.DEBUG, name=None, message=None):
    if func is None:
        return partial(logged, level=level, name=name, message=message)

    logname = name if name else func.__module__
    log = logging.getLogger(logname)
    logmsg = message if message else func.__name__

    @wraps(func)
    def wrapper(*args, **kwargs):
        log.log(level, logmsg)
        return func(*args, **kwargs)
    return wrapper


@logged
def add(x, y):
    return x+y

@logged(level=logging.CRITICAL, name='exxample')
def spam():
    print("Spam!")

add(1,2)
spam()

#########
# 装饰器的用
@logged
def add(x, y):
    return x+y

#######  ===>
def add(x, y):
    return x + y
add = logged(add)

##### 如果是带参数的装饰器
@logged(level=logging.CRITICAL, name='exxample')
def spam():
    print("Spam!")

#######  ===>
def spam():
    print("Spam!")
spam = logged(level=logging.CRITICAL, name='exxample')(spam)