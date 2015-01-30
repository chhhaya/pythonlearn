class Person:
    def __init__(self, first_name):
        self.first_name = first_name

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        if not isinstance(value, str):
            raise TypeError("expected a string")
        self._first_name = value

    @first_name.deleter
    def first_name(self):
        raise AttributeError("can not delete attribute")

# 另一个种
class Person2:
    def __init__(self, first_name):
        self.set_first_name(first_name)

    def get_first_name(self):
        return self._first_name

    def set_first_name(self, value):
        if not isinstance(value, str):
            raise TypeError("expected a string")
        self._first_name = value

    def del_first_name(self):
        raise AttributeError("can not delete attribute")

    name = property(set_first_name, get_first_name, del_first_name)

a = Person('chhaya')
print(a.first_name)
a.first_name = 'hello'
# del a.first_name

# 不建议用很多set 和get

import math
class Circle:
    def __init__(self, radius):
        self.radius = radius

    @property
    def area(self):
        return math.pi * self.radius ** 2

    @property
    def perimeter(self):
        return 2 * math.pi * self.radius

c = Circle(4.0)
print(c.radius)
print(c.area)
print(c.perimeter)