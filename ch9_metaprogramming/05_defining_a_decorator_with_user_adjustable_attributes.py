import logging
from functools import wraps, partial

def attach_wrapper(obj, func=None):
    if func is None:
        return partial(attach_wrapper, obj)
    setattr(obj, func.__name__, func)
    return func

def logged(level, name=None, message=None):
    def decorate(func):
        logname = name if name else func.__module__
        log = logging.getLogger(logname)
        logmsg = message if message else func.__name__

        @wraps(func)
        def wrapper(*args, **kwargs):
            log.log(level, logmsg)
            return func(*args, **kwargs)


        @attach_wrapper(wrapper)
        def set_level(newlevel):
            nonlocal level
            level = newlevel

        @attach_wrapper(wrapper)
        def set_message(newmsg):
            nonlocal logmsg
            logmsg = newmsg

        return wrapper
    return decorate


@logged(logging.DEBUG)
def add(x, y):
    return x+y

@logged(logging.CRITICAL, 'exxample')
def spam():
    print("Spam!")

logging.basicConfig(level=logging.DEBUG)
add(1,2)
# DEBUG:__main__:add
add.set_message(' add called ')
add(2, 3)
# DEBUG:__main__: add called
add.set_level(logging.INFO)
add(3, 4)
# INFO:__main__: add called
spam()