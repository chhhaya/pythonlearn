import time


class Date:
    # 主构造器
    def __init__(self, y, m, d):
        self.year = y
        self.month = m
        self.day = d

    # 可选构造器, 类方法
    @classmethod
    def today(cls):
        t = time.localtime()
        return cls(t.tm_year, t.tm_mon, t.tm_mday)

a = Date(2015, 3, 4)
b = Date.today()

# 可继承
class NewDate(Date):
    pass

nb = NewDate.today()