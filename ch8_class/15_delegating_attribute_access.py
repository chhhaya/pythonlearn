# method少的时候：

class A:
    def spam(self, x):
        pass

    def foo(self):
        pass

class B:
    def __init__(self):
        self._a = A()

    def spam(self, x):
        return self._a.spam(x)

    def foo(self):
        return self._a.foo()

    def bar(self):
        pass


# method多了
class AA:
    def spam(self, x):
        pass

    def foo(self):
        pass

class BB:
    def __init__(self):
        self._a = AA()

    def bar(self):
        pass

    # 拿到A所有的方法
    def __getattr__(self, item):
        return getattr(self._a, item)

b = BB()
b.bar()
b.foo()
b.spam(1)

# 代理模式

class Proxy:
    def __init__(self, obj):
        self._obj = obj

    def __getattr__(self, item):
        print('getattr', item)
        return getattr(self._obj, item)

    def __setattr__(self, key, value):
        if key.startswith('_'):
            super().__setattr__(key, value)
        else:
            print('setattr', key, value)
            setattr(self._obj, key, value)

    def __delattr__(self, item):
        if item.startswith('_'):
            super().__delattr__(item)
        else:
            print('delete', item)
            delattr(self._obj, item)

class Spam():
    def __init__(self, x):
        self.x = x

    def bar(self, y):
        print('Spam.bar', self.x, y)

s = Spam(2)
p = Proxy(s)
# getattr x

print(':', p.x)
# : 2
p.bar(3)
# getattr bar
# Spam.bar 2 3
p.x = 37
# setattr x 37



# 另一种用继承的方式
class A:
    def spam(self, x):
        print('a.spam', x)

    def foo(self):
        print('a.foo')

class B(A):
    def spam(self, x):
        print('b.spam')
        super().spam(x)

    def bar(self):
        print('b.bar')

#