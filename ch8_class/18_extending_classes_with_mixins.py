# 给内置类型，增加了很多其他功能

class LoggedMappingMixin:
    """
    get/set/del的时候能打日志
    """
    __slots__ = ()

    def __getitem__(self, item):
        print('get', item)
        return super().__getitem__(item)

    def __setitem__(self, key, value):
        print('set {} = {!r}'.format(key, value))
        super().__setitem__(key, value)

    def __delitem__(self, key):
        print('delete', key)
        super().__delitem__(key)

class LoggedDict(LoggedMappingMixin, dict):
    pass

d = LoggedDict()
d['x'] = 23
# set x = 23
d['x']
# get x
del d['x']
# delete x

class SetOnceMappingMixin:
    __slots__ = ()

    def __setitem__(self, key, value):
        if key in self:
            raise KeyError(str(key) + ' already set')
        return super().__setitem__(key, value)

from collections import defaultdict
class SetOnceDict(SetOnceMappingMixin, defaultdict):
    pass

dd = SetOnceDict(list)
dd['x'].append(2)
dd['x'].append(10)
# dd['x'] = 10
# KeyError: 'x already set'

class StringKeysMappingMixin:
    __slots__ = ()

    def __setitem__(self, key, value):
        if not isinstance(key, str):
            raise TypeError('keys must be strings')
        super().__setitem__(key, value)

from collections import OrderedDict
class StringOrderDict(StringKeysMappingMixin,
                      SetOnceMappingMixin,
                      OrderedDict):
    pass

d = StringOrderDict()
d['x'] = 23
# d[2] = 23
# TypeError: keys must be strings
# d['x'] = 3
# KeyError: 'x already set'



## 装饰器的方式：
def LoggedMapping(cls):
    cls_getitem = cls.__getitem__
    cls_setitem = cls.__setitem__
    cls_delitem = cls.__delitem__

    def __getitem__(self, key):
        print('Getting ' + str(key))
        return cls_getitem(self, key)

    def __setitem__(self, key, value):
        print('set {} = {!r}'.format(key, value))
        return cls_setitem(self, key, value)

    def __delitem__(self, key):
        print('del ', key)
        return cls_delitem(self, key)

    cls.__getitem__ = __getitem__
    cls.__setitem__ = __setitem__
    cls.__delitem__ = __delitem__
    return cls

@LoggedMapping
class LoggedDict(dict):
    pass

print('-----')
ld = LoggedDict()
ld['xx'] = 'ss'
# set xx = 'ss'
print(ld['xx'])
# Getting xx