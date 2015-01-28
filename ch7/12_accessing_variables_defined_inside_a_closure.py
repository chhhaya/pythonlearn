# 获得closure的里面的变量

def sample():
    n = 0  # 变量对外不可见
    def func():
        print('n=', n)

    def get_n():
        return n

    def set_n(value):
        nonlocal n
        n = value

    func.get_n = get_n ## attach
    func.set_n = set_n

    return func

f = sample()
f()
# n=0
f.set_n(10)

f()
# n=10
print(f.get_n())
# 10


import sys
class ClosureInstance:
    def __init__(self, locals=None):
        if locals is None:
            locals = sys._getframe(1).f_locals
        self.__dict__.update((key, value) for key, value in locals.items() if callable(value))

    def __len__(self):
        return self.__dict__['__len__']()

def Stack():
    items = []

    def push(item):
        items.append(item)

    def pop():
        return items.pop()

    def __len__():
        return len(items)

    return ClosureInstance()

s = Stack()
print(s)
s.push(10)
s.push(20)
s.push('hello')
print(len(s))

print(s.pop())
print(s.pop())
print(s.pop())

# <__main__.ClosureInstance object at 0x10208b390>
# 3
# hello
# 20
# 10


# 这种比用class版的stack快