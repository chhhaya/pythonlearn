class A:
    def spam(self):
        print('A.spam')

class B(A):
    def spam(self):
        print('B.spam')
        super().spam()

b = B()
b.spam()

# B.spam
# A.spam

# 常用一
# init 中

class C:
    def __init__(self):
        self.x = 0

class D(C):
    def __init__(self):
        super().__init__()
        self.y = 0

d = D()
print(d.x)
# 0

# 常用二
# override父类方法

class Proxy:
    def __init__(self, obj):
        self._obj = obj

    def __getattr__(self, item):
        return getattr(self._obj, item)

    def __setattr__(self, key, value):
        if key.startswith('_'):
            super().__setattr__(key, value)  # call original __setattr__
        else:
            setattr(self._obj, key, value)

class E(A, C):
    pass

print(E.__mro__)
# (<class '__main__.E'>, <class '__main__.A'>, <class '__main__.C'>, <class 'object'>)
