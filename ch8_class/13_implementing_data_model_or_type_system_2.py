# 检查类型

class Descriptor:
    def __init__(self, name=None, **opts):
        self.name = name
        for key, value in opts.items():
            setattr(self, key, value)

    def __set__(self, instance, value):
        instance.__dict__[self.name] = value

def Typed(expected_type, cls=None):
    if cls is None:
        return lambda cls: Typed(expected_type, cls)

    super_set = cls.__set__
    def __set__(self, instance, value):
        if not isinstance(value, expected_type):
            raise TypeError('error type')
        super_set(self, instance, value)
    cls.__set__ = __set__
    return cls

def Unsigned(cls):
    super_set = cls.__set__
    def __set__(self, instance, value):
        if value < 0:
            raise ValueError('can not < 0')
        super_set(self, isinstance, value)
    cls.__set__ == __set__
    return cls

def MaxSized(cls):
    super_init = cls.__init__
    def __init__(self, name=None, **opts):
        if 'size' not in opts:
            raise ValueError('missing size')
        super_init(self, name, **opts)
    cls.__init__ = __init__

    super_set = cls.__set__
    def __set__(self, instance, value):
        if len(value) > self.size:
            raise ValueError('size must < ')
        super_set(self, instance, value)
    cls.__set__ = __set__
    return cls

@Typed(int)
class Integer(Descriptor):
    pass

@Unsigned
class UnsignedInteger(Integer):
    pass

@Typed(float)
class Float(Descriptor):
    pass

@Unsigned
class UnsignedFloat(Float):
    pass

@Typed(str)
class String(Descriptor):
    pass

@MaxSized
class SizedString(String):
    pass


class Stock:
    name = SizedString('name', size=10)
    shares = UnsignedInteger('shares')
    price = UnsignedFloat('price')
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price=price

s = Stock('ACD', 2, 3.6)
s.shares=3
# s.shares=2.9   # Exception
# s.price='a lot'
# TypeError: unorderable types: str() < int()
# s.name = 'ABNHEKUHHNMOJJ'
# ValueError: value must < 10

