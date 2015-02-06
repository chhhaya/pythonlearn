import collections

class A(collections.Iterable):
    pass

# a = A()
# TypeError: Can't instantiate abstract class A with abstract methods __iter__
# 必须实现 __iter__方法

# collections.Sequence()
# TypeError: Can't instantiate abstract class Sequence with abstract methods __getitem__, __len__
# Sequence() 必须实现 __getitem__, __len__

import bisect

class SortedItems(collections.Sequence):
    def __init__(self, initial=None):
        self._items = sorted(initial) if initial is not None else []

    def __getitem__(self, index):
        return self._items[index]

    def __len__(self):
        return len(self._items)

    # 插入到正确的位置，一直保证顺序排列
    def add(self, item):
        bisect.insort(self._items, item)

items = SortedItems([5, 1, 3])
print(list(items))
# [1, 3, 5]
print(items[0], items[-1])
# 1 5
items.add(4)
print(list(items))
# [1, 3, 4, 5]
print(3 in items)
# True
print(len(items))
# 4
for i in items:
    print(i)

print(isinstance(items, collections.Iterable))
print(isinstance(items, collections.Sequence))
print(isinstance(items, collections.Container))
print(isinstance(items, collections.Sized))
print(isinstance(items, collections.Mapping))
# False

