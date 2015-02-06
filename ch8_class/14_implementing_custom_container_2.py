import collections

class Items(collections.MutableSequence):
    def __init__(self, initial=None):
        self._items = list(initial) if initial is not None else []

    def __getitem__(self, item):
        print("Get", item)
        return self._items[item]

    def __setitem__(self, key, value):
        print("Set", key, value)
        self._items[key] = value

    def __delitem__(self, key):
        print("delete", key)
        del self._items[key]

    def insert(self, index, value):
        print('insert', index, value)
        self._items.insert(index, value)

    def __len__(self):
        print('Len')
        return len(self._items)

items = Items([2, 3, 4])
print(len(items))
# Len
# 3

items.append(0)
# insert 3 0

items.count(4)
# Get 0
# Get 1
# Get 2
# Get 3
# Get 4
items.remove(0)
# Get 0
# Get 1
# Get 2
# Get 3
# delete 3