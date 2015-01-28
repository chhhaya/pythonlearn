
# 方法一
def apply_async(func, args, *, callback):
    result = func(*args)
    callback(result)

def print_result(result):
    print("Got:", result)

def add(x, y):
    return x+y

apply_async(add, (2, 3), callback=print_result)
# Got: 5


# 方法二
class ResultHandler:
    def __init__(self):
        self.sequence = 0

    def handler(self, result):
        self.sequence += 1
        print('[{}] Got: {}'.format(self.sequence, result))

r = ResultHandler()
apply_async(add, (2, 3), callback=r.handler)
# [1] Got: 5


# 方法三
def make_handler():
    sequence = 0
    def handler(result):
        nonlocal sequence   # 必须nonlocal
        sequence += 1
        print('[{}] Got: {}'.format(sequence, result))
    return handler

handler = make_handler()
apply_async(add, (2, 3), callback=handler)
# [1] Got: 5


# 方法四
# 协同程序，
# TODO 看不懂
def make_handler():
    sequence = 0
    while True:
        result = yield
        sequence += 1
        print('[{}] Got: {}'.format(sequence, result))
handler = make_handler()
next(handler)
apply_async(add, (2, 3), callback=handler.send)
# [1] Got: 5

# 方法五
class SequenceNo:
    def __init__(self):
        self.sequence = 0

def handler(result, seq):
    seq.sequence += 1
    print('[{}] Got: {}'.format(seq.sequence, result))

seq = SequenceNo()
from functools import partial
apply_async(add, (2, 3), callback=partial(handler, seq=seq))
# [1] Got: 5
