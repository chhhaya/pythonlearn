class Date:
    def __init__(self, y, m, d):
        self.year = y
        self.month = m
        self.day = d

d = Date.__new__(Date)
print(d)
# <__main__.Date object at 0x1006f2eb8>
# print(d.year)
# AttributeError: 'Date' object has no attribute 'year'

# 需要自己去设置属性

date = {'year': 2012, 'month': 3, 'day':3}
for k, v in date.items():
    setattr(d, k, v)
print(d.day)
# 3

