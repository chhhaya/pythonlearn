import math
# 基础版
class Structure:
    _fields = []
    def __init__(self, *args):
        if len(args) != len(self._fields):
            raise TypeError('Expteced {} arguments'.format(len(self._fields)))

        for name, value in zip(self._fields, args):
            setattr(self, name, value)

# 可以带kwargs版
class Structuree:
    _fields = []
    def __init__(self, *args, **kwargs):
        if len(args) > len(self._fields):
            raise TypeError('Expteced {} arguments'.format(len(self._fields)))

        for name, value in zip(self._fields, args):
            setattr(self, name, value)

        for name in self._fields[len(args):]:
            setattr(self, name, kwargs.pop(name))

        if kwargs:
            raise TypeError("invalid argument(s): {}".format(','.join(kwargs)))

# 可以带kwargs，并且不放在fields版
class Structureee:
    _fields = []
    def __init__(self, *args, **kwargs):
        if len(args) != len(self._fields):
            raise TypeError('Expteced {} arguments'.format(len(self._fields)))

        for name, value in zip(self._fields, args):
            setattr(self, name, value)

        extra_args = kwargs.keys() - self._fields
        for name in extra_args:
            setattr(self, name, kwargs.pop(name))

        if kwargs:
            raise TypeError("invalid argument(s): {}".format(','.join(kwargs)))

# frame hack版
def init_formlocals(self):
    import sys
    locs = sys._getframe(1).f_locals
    for k, v in locs.items():
        if k != 'self':
            setattr(self, k, v)



if __name__ == '__main__':
    class Stock(Structure):
        _fields = ['name', 'shares', 'price']

    class Circle(Structure):
        _fields = ['radius']
        def area(self):
            return math.pi * self.radius ** 2

    class Stockk(Structuree):
        _fields = ['name', 'shares', 'price']

    class Stockkk:
        def __init__(self, name, shares, price):
            init_formlocals(self)

    s = Stock('AMC', 2, 32.2)
    c = Circle(20)
    print(c.area())
    # 1256.6370614359173
    # s2 = Stock('CCC', 2)
    s2 = Stockk('ACM', shares=2, price=2.0)

    s3 = Stockkk('ACM', 2, 2.0)
    print(s3.shares)
    # 2