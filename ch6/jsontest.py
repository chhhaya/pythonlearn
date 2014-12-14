import json

data = {
    'name': 'AMEC',
    'shares': 100,
    'price': 543.32,
    'nn': None
}

# json转字符串
json_str = json.dumps(data)
print(json_str)

# 字符串转json
data = json.loads(json_str)
print(data)

# 写到json文件
with open('data.json', 'w') as f:
    json.dump(data, f)

# 从json文件读
with open('data.json') as f:
    data = json.load(f)
    print(data)

# python --> json
# False ->  false
# True -> true
# None -> null


# 放入ordered字典
from collections import OrderedDict
s = json.dumps(data)
data = json.loads(s, object_pairs_hook=OrderedDict)
print(data)
# OrderedDict([('shares', 100), ('nn', None), ('price', 543.32), ('name', 'AMEC')])

# json字典转成python字典
# class JSONObject:
#     def __init__(self, d):
#         self.__dict__ = d
#
# data = json.loads(s, object_hook=JSONObject)
# print(data.name)
# print(data.price)

# 其他参数
print(json.dumps(data, indent=4))
# {
#     "name": "AMEC",
#     "nn": null,
#     "price": 543.32,
#     "shares": 100
# }
print(json.dumps(data, sort_keys=True))
# {"name": "AMEC", "nn": null, "price": 543.32, "shares": 100}

# 要dumps不是字典的类
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def serialize_instance(obj):
    d = {'__classname__': type(obj).__name__}
    d.update(vars(obj))
    return d

classes = {
    'Point': Point
}

def unserialize_instance(d):
    clsname = d.pop('__classname__', None)
    if clsname:
        cls = classes[clsname]
        obj = cls.__new__(cls)
        for key, value in d.items():
            setattr(obj, key, value)
        return obj
    else:
        return d
p = Point(2, 3)
s = json.dumps(p, default=serialize_instance)
# {"x": 2, "__classname__": "Point", "y": 3}
a = json.loads(s, object_hook=unserialize_instance)
print(a)
# <__main__.Point object at 0x102197ac8>
print(a.x, a.y)
# 2 3