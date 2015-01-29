# 就是支持with
# 必须实现__enter__()和__exit__()两个方法

from socket import socket, AF_INET, SOCK_STREAM

class LazyConnection:
    def __init__(self, address, family=AF_INET, type=SOCK_STREAM):
        self.address = address
        self.family = family
        self.type = type
        self.socket = None

    def __enter__(self):
        print('enter')
        if self.socket is not None:
            raise RuntimeError('Already connected')
        self.socket = socket(self.family, self.type)
        self.socket.connect(self.address)
        return self.socket

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('bye')
        self.socket.close()
        self.socket = None

from functools import partial

conn = LazyConnection(('www.python.org', 80))
with conn as s:
    s.send(b'GET /index.html HTTP/1.0\r\n')
    s.send(b'Host: www.python.org\r\n')
    s.send(b'\r\n')
    resp = b''.join(iter(partial(s.recv, 8192), b''))


# ==========================================
# 可嵌套版本

class LazyConnections:
    def __init__(self, address, family=AF_INET, type=SOCK_STREAM):
        self.address = address
        self.family = family
        self.type = type
        self.connections = []

    def __enter__(self):
        print('enter')
        sock = socket(self.family, self.type)
        sock.connect(self.address)
        self.connections.append(sock)
        return sock

    def __exit__(self, exc_type, exc_val, exc_tb):
        """

        :param exc_type:   exception_type
        :param exc_val:    exception_value
        :param exc_tb:     exception traceback
        :return:
        """
        print('bye')
        self.connections.pop().close()

