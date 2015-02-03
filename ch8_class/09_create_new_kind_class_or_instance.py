class Integer:
    def __init__(self, name):
        self.name = name

    def __get__(self, instance, owner):
        print('get')
        if instance is None:   # 类调用的时候
            return self
        else:
            return instance.__dict__[self.name]   # 实例调用的时候

    def __set__(self, instance, value):
        print('set')
        if not isinstance(value, int):
            raise TypeError(' expected int')
        instance.__dict__[self.name] = value

    def __delete__(self, instance):
        print('del')
        del instance.__dict__[self.name]

class Point:
    x = Integer('x')
    y = Integer('y')
    def __init__(self, x, y):
        self.x = x
        self.y = y

p = Point(2, 3)
print(p.x)
p.x = 4
# p.y = 3.4
del p.y
# print(p.y)



# 类型检查的

class Typed:
    def __init__(self, name, expected_type):
        self.name = name
        self.expected_type = expected_type

    def __get__(self, instance, owner):
        if instance is None:
            return self
        else:
            return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if not isinstance(value, self.expected_type):
            raise TypeError(' Expected :' + str(self.expected_type))
        instance.__dict__[self.name] = value

    def __delete__(self, instance):
        del instance.__dict__[self.name]

def typeassert(**kwargs):
    def decorate(cls):
        for name, expected_type in kwargs.items():
            setattr(cls, name, Typed(name, expected_type))
        return cls
    return decorate

@typeassert(name=str, shares=int, price=float)
class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

sock = Stock('xxx', 12, 12.2)
# sock = Stock('xxx', 12, 12)