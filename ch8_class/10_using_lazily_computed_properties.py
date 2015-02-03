class LazyProperty:
    def __init__(self, func):
        self.func = func

    def __get__(self, instance, owner):
        if instance is None:
            return self
        else:
            value = self.func(instance)
            setattr(instance, self.func.__name__, value)
            return value

import math
class Circle:
    def __init__(self, rad):
        self.rad = rad

    @LazyProperty
    def area(self):
        print('Computing area')
        return math.pi * self.rad ** 2

    @LazyProperty
    def perimeter(self):
        print('computing perimeter')
        return 2 * math.pi * self.rad

c = Circle(4.0)
print(c.rad)
# 4.0
print(c.area)
# Computing area
# 50.26548245743669
print(c.area)
# 50.26548245743669
print(c.perimeter)
# computing perimeter
# 25.132741228718345
print(c.perimeter)
# 25.132741228718345