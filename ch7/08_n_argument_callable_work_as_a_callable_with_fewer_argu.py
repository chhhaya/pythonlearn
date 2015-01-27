def spam(a, b, c, d):
    print(a, b, c, d)

# 通过给固定默认参数，减少参数个数
from functools import partial
s1 = partial(spam, 1)
s1(2, 3, 4)
# 1 2 3 4
s1(4, 5, 6)
# 1 4 5 6
s2 = partial(spam, d=42)
s2(1, 2, 3)
# 1 2 3 42
s2(4, 5, 6)
# 4 5 6 42
s3 = partial(spam, 1, 2, d=42)
s3(5)
# 1 2 5 42


# 计算一些点到某个点的距离
points = [(1, 2), (3, 4), (5, 6), (7, 8)]
import math
def distance(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return math.hypot(x2-x1, y2-y1)

pt = (4, 3)
points.sort(key=partial(distance, pt))
print(points)
# [(3, 4), (1, 2), (5, 6), (7, 8)]

def output_result(result, log=None):
    if log is not None:
        log.debug('Got: %r', result)

def add(x, y):
    return x+y


from socketserver import StreamRequestHandler, TCPServer
class EchoHandler2(StreamRequestHandler):
    def handle(self):
        for line in self.rfile:
            self.wfile.write(b'Got:' + line)

class EchoHandler(StreamRequestHandler):
    def __init__(self, *args, ack, **kwargs):
        self.ack = ack
        print(self.ack)
        super().__init__(*args, **kwargs)

    def handle(self):
        for line in self.rfile:
            self.wfile.write(self.ack + line)

if __name__ == '__main__':
    import logging
    from multiprocessing import Pool
    from functools import partial

    logging.basicConfig(level=logging.DEBUG)
    log = logging.getLogger('test')

    p = Pool()
    p.apply_async(add, (3, 4), callback=partial(output_result, log=log))
    # 另一种方案
    p.apply_async(add, (3, 4), callback=lambda result: output_result(result, log))
    # 下面这个不行是因为，callback只能传一个参数进去
    # p.apply_async(add, (3, 4), callback=output_result(log=log))
    p.close()
    p.join()

    # serv = TCPServer(('', 5000), EchoHandler2)
    # serv = TCPServer(('', 5001), partial(EchoHandler, ack=b'RECEIVED:'))
    # 如果不用partial的话，ack参数没地方传进去。
    # serv.serve_forever()