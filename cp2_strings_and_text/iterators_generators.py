# 4.1 ## 手动消费一个iterator
# (1)
# with open("/etc/hosts") as f:
#     try:
#         while True:
#             line = next(f)
#             print(line, end='')
#     except StopIteration:
#         pass
# (2)
# with open("/etc/hosts") as f:
#     while True:
#         line = next(f, None)
#         if line is None:
#             break
#         print(line, end="")

# >>> items = [1,2,3]
# >>> it = iter(items)  # 调用 items.__iter__()
# >>> next(it)  # 调用 it.__next__()
# 1
# >>> next(it)
# 2
# >>> next(it)
# 3
# >>> next(it)
# Traceback (most recent call last):
#   File "<input>", line 1, in <module>
# StopIteration


# 4.2 ## 授权迭代器
class Node:
    def __init__(self, value):
        self._value = value
        self._children = []

    def __repr__(self):
        return 'None({!r})'.format(self._value)

    def add_child(self, node):
        self._children.append(node)

    def __iter__(self):
        return iter(self._children)

root = Node(0)
c1 = Node(1)
c2 = Node(2)
root.add_child(c1)
root.add_child(c2)
for ch in root:
    print(ch)
# None(1)
# None(2)


# 4.3 ## 使用生成器create新的迭代器pattern
# float版的range
def frange(start, stop, step):
    x = start
    while x < stop:
        yield x
        x += step
for n in frange(3.4, 5.6, 0.5):
    print(n)
# 3.4
# 3.9
# 4.4
# 4.9
# 5.4


# 4.4 ## 迭代器协议
class Node:
    def __init__(self, value):
        self._value = value
        self._children = []

    def __repr__(self):
        return 'None({!r})'.format(self._value)

    def add_child(self, node):
        self._children.append(node)

    def __iter__(self):
        return iter(self._children)

    def depth_first(self):
        yield self
        for c in self:
            yield from self.depth_first()

root = Node(0)
c1 = Node(1)
c2 = Node(2)
root.add_child(c1)
root.add_child(c2)
c1.add_child(Node(3))
c1.add_child(Node(4))
c2.add_child(Node(5))
for ch in root.depth_first():
    print(ch)
