# 抽象基类
from abc import ABCMeta, abstractmethod


class IStream(metaclass=ABCMeta):
    @abstractmethod
    def read(self, maxbytes=-1):
        pass

    @abstractmethod
    def write(self, data):
        pass

# 必须被继承，不能被实例化

class SocketStream(IStream):
    def read(self, maxbytes=-1):
        pass

    def write(self, data):
        pass

# 检查只有某类接口才能用
def serialize(obj, stream):
    if not isinstance(stream, IStream):
        raise TypeError('Expected an IStream')
    pass

# ABC也能注册
import io
IStream.register(io.IOBase)
f = open('foo.txt')
isinstance(f, IStream)
# True

# 抽象方法也能用于静态方法，类方法，类属性
class A(metaclass=ABCMeta):
    @property
    @abstractmethod
    def name(self):
        pass

    @name.setter
    @abstractmethod
    def name(self, value):
        pass

    @classmethod
    @abstractmethod
    def method1(cls):
        pass

    @staticmethod
    @abstractmethod
    def method2():
        pass