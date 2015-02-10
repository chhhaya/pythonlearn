import logging
from functools import wraps

def logged(level, name=None, message=None):
    def decorate(func):
        logname = name if name else func.__module__
        log = logging.getLogger(logname)
        logmsg = message if message else func.__name__

        @wraps(func)
        def wrapper(*args, **kwargs):
            log.log(level, logmsg)
            return func(*args, **kwargs)
        return wrapper
    return decorate

@logged(logging.WARN)
def add(x, y):
    return x+y

@logged(logging.CRITICAL, 'exxample')
def spam():
    print("Spam!")

add(1,2)
spam()