# 检查类型

class Descriptor:
    def __init__(self, name=None, **opts):
        self.name = name
        for key, value in opts.items():
            setattr(self, key, value)

    def __set__(self, instance, value):
        instance.__dict__[self.name] = value


class Typed(Descriptor):
    expected_type = type(None)

    def __set__(self, instance, value):
        if not isinstance(value, self.expected_type):
            raise TypeError('expected ' + str(self.expected_type))
        super().__set__(instance, value)

class Unsigned(Descriptor):
    def __set__(self, instance, value):
        if value < 0:
            raise ValueError('Expecetd >= 0')
        super().__set__(instance, value)

class MaxSized(Descriptor):
    def __init__(self, name=None, **opts):
        if 'size' not in opts:
            raise TypeError('missing size option')
        super().__init__(name, **opts)

    def __set__(self, instance, value):
        if len(value) >= self.size:
            raise ValueError('value must < ' + str(self.size))
        super().__set__(instance, value)

class Integer(Typed):
    expected_type = int

class UnsignedInteger(Unsigned, Integer):
    pass

class Float(Typed):
    expected_type = float

class UnsignedFloat(Unsigned, Float):
    pass

class String(Typed):
    expected_type = str

class SizedString(MaxSized, String):
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


# 简化一: 装饰器
def check_attributes(**kwargs):
    def decorate(cls):
        for key, value in kwargs.items():
            if isinstance(value, Descriptor):
                value.name = key
                setattr(cls, key, value)
            else:
                setattr(cls, key, value(key))
        return cls
    return decorate

@check_attributes(name=SizedString(size=8),
                  shares=UnsignedInteger,
                  price=UnsignedFloat)

class Stocks:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

s = Stocks('ACD', 2, 3.6)
s.shares=3
# s.shares=2.9   # Exception

# 简化二，metaclass

class checkedmeta(type):
    def __new__(cls, clsname, bases, methods):
        for key, value in methods.items():
            if isinstance(value, Descriptor):
                value.name = key
        return type.__new__(cls, clsname, bases, methods)

class Stocksss(metaclass=checkedmeta):
    name = SizedString(size=8)
    shares = UnsignedInteger()
    price = UnsignedFloat()
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

s = Stocksss('ACD', 2, 3.6)
s.shares=3
# s.shares=2.9   # Exception