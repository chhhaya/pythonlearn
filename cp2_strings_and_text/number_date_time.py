# coding:utf8

# 3.1 ## 小数变整数
# 总是向最近的偶数靠拢
# >>> round(1.23, 1)
# 1.2
# >>> round(1.25, 1)
# 1.2
# >>> round(-1.25, 1)
# -1.2

# 可以精确到10，100，1000等
# >>> a = 1624534
# >>> round(a, -1)
# 1624530
# >>> round(a, -3)
# 1625000

# 如果只是为了输出的话, 用format更好
# >>> x = 1.23455
# >>> format(x, '0.2f')
# '1.23'
# >>> format(x, '0.3f')
# '1.235'
# >>> 'value is {:0.3f}'.format(x)
# 'value is 1.235'

# 修复计算结果
# >>> a = 2.1
# >>> b = 4.2
# >>> a+b
# 6.300000000000001
# >>> c = a+b
# >>> c = round(c, 2)
# >>> c
# 6.3


# 3.2 ## 精确的十进制计算
from decimal import Decimal
a = Decimal('4.2')
b = Decimal('2.1')
a + b
# Decimal('6.3')
(a+b) == Decimal('6.3')
# True

# 可以指定计算精度
from decimal import localcontext
a = Decimal('1.3')
b = Decimal('1.7')
print(a/b)
with localcontext() as ctx:
    ctx.prec = 3
    print(a/b)
# 0.7647058823529411764705882353
# 0.765
with localcontext() as ctx:
    ctx.prec = 50
    print(a/b)
# 0.76470588235294117647058823529411764705882352941176

# 一般的计算用float比decimal快很多。
# 精度要求特别高的才不能用float
nums = [1.23e+18, 1, -1.23e+18]
print(sum(nums))
# 0.0
import math
print(math.fsum(nums))
# 1.0


# 3.3 ## 数字格式化输出
# format格式： '[<>^]?width[,]?(.digits)?'
# >>> x = 1234.56789
# >>> format(x, '0.2f')
# '1234.57'
# >>> format(x, '>10.1f')
# '    1234.6'
# >>> format(x, '<10.1f')
# '1234.6    '
# >>> format(x, '^10.1f')
# '  1234.6  '
# >>> format(x, ',')
# '1,234.56789'
# >>> format(x, '0,.1f')
# '1,234.6'
# >>> format(x, 'e')
# '1.234568e+03'
# >>> format(x, 'E')
# '1.234568E+03'


# 3.4 ## 二进制，八进制，十六进制
# >>> bin(x)
# '0b10011010010'
# >>> format(x, 'b')
# '10011010010'
# >>> oct(x)
# '0o2322'
# >>> format(x, 'o')
# '2322'
# >>> hex(x)
# '0x4d2'
# >>> format(x, 'x')
# '4d2'

# 无符号数
# >>> x = -1234
# >>> format(2**32 + x, 'b')
# '11111111111111111111101100101110'

# 要把其他进制转成十进制，只要
# >>> int('4d2', 16)
# 1234
# >>> int('100111000100', 2)
# 2500

# 表示八进制前面要加0o
# 表示十六进制前面要加0x


# 3.5 ## 从二进制pack和unpack大整数
# >>> data = b'\x00\x124V\x00x\x90\xab\x00\xcd\xef\x01\x00#\x004'
# >>> len(data)
# 16
# >>> int.from_bytes(data, 'little')
# 69120565665751139577663547927094891008
# >>> int.from_bytes(data, 'big')
# 94522842520747284487117727783387188

# 反过来
# >>> x = 94522842520747284487117727783387188
# >>> x.to_bytes(16, 'big')
# b'\x00\x124V\x00x\x90\xab\x00\xcd\xef\x01\x00#\x004'
# >>> x.to_bytes(16, 'little')
# b'4\x00#\x00\x01\xef\xcd\x00\xab\x90x\x00V4\x12\x00'

# 也可以用struct来unpack
# >>> import struct
# >>> hi, lo = struct.unpack('>QQ', data)
# >>> (hi << 64) + lo
# 94522842520747284487117727783387188

# 如果要pack一个整数，但是长度不合适
# x = 523 ** 23
# >>> x
# 335381300113661875107536852714019056160355655333978849017944067
# >>> x.to_bytes(16, 'little')
# Traceback (most recent call last):
#   File "<input>", line 1, in <module>
# OverflowError: int too big to convert
# >>> x.bit_length()
# 208
# >>> nbytes, rem = divmod(x.bit_length(), 8)
# >>> if rem:
# ...     nbytes += 1
# ...
# >>> x.to_bytes(nbytes, 'little')
# b'\x03X\xf1\x82iT\x96\xac\xc7c\x16\xf3\xb9\xcf\x18\xee\xec\x91\xd1\x98\xa2\xc8\xd9R\xb5\xd0'

# 3.6 ## 处理复数
# >>> a = complex(2, 4)
# >>> b = 3 - 5j
# >>> a
# (2+4j)
# >>> b
# (3-5j)
# >>> a.real
# 2.0
# >>> a.imag
# 4.0
# >>> a.conjugate()
# (2-4j)

# 用cmath计算复数
# >>> import cmath
# >>> cmath.sin(a)
# (24.83130584894638-11.356612711218174j)
# >>> cmath.sqrt(-1)
# 1j

# 3.7 ## 无穷数和NaN
# >>> a = float('inf')
# >>> a
# inf
# >>> b = float('-inf')
# >>> b
# -inf
# >>> c = float('nan')
# >>> c
# nan

# 判断是否是inf和nan
# >>> import math
# >>> math.isinf(a)
# True
# >>> math.isnan(c)
# True


# 3.8 ## 计算分数

# >>> from fractions import Fraction
# >>> a = Fraction(5, 4)
# >>> b = Fraction(7, 16)
# >>> print (a + b)
# 27/16
# >>> print(a * b)
# 35/64
# >>> c = a*b
# >>> c.numerator  # 分子
# 35
# >>> c.denominator  # 分母
# 64
# 分数转小数
# >>> float(c)
# 0.546875
# >>> print(c.limit_denominator(8))
# 4/7
# 小数转分数
# >>> x = 3.75
# >>> y = Fraction(*x.as_integer_ratio())
# >>> y
# Fraction(15, 4)

# 3.9 ## 计算数组
# python的list：
# >>> x = [1,2,3,4]
# >>> y = [5,6,7,8]
# >>> x + y
# [1, 2, 3, 4, 5, 6, 7, 8]
# >>> x * 2
# [1, 2, 3, 4, 1, 2, 3, 4]
# >>> x + 10
# Traceback (most recent call last):
#   File "<input>", line 1, in <module>
# TypeError: can only concatenate list (not "int") to list

# 数字数组：
import numpy as np
ax = np.array([1,2,3,4])
ay = np.array([5,6,7,8])
# >>> ax * 2
# array([2, 4, 6, 8])
# >>> ax + 10
# array([11, 12, 13, 14])
# >>> ax + ay
# array([ 6,  8, 10, 12])
# >>> ax * ay
# array([ 5, 12, 21, 32])

def f(x):
    return 3*x**2 - 2*x +7
print(f(ax))
# [ 8 15 28 47]
# 这种比循环算快
# >>> np.sqrt(ax)
# array([ 1.        ,  1.41421356,  1.73205081,  2.        ])
# >>> np.cos(ax)
# array([ 0.54030231, -0.41614684, -0.9899925 , -0.65364362])

# 算多维素组
# >>> grid = np.zeros(shape=(100, 100), dtype=float)
# >>> grid
# array([[ 0.,  0.,  0., ...,  0.,  0.,  0.],
#        [ 0.,  0.,  0., ...,  0.,  0.,  0.],
#        [ 0.,  0.,  0., ...,  0.,  0.,  0.],
#        ...,
#        [ 0.,  0.,  0., ...,  0.,  0.,  0.],
#        [ 0.,  0.,  0., ...,  0.,  0.,  0.],
#        [ 0.,  0.,  0., ...,  0.,  0.,  0.]])
# >>> grid += 10
# >>> grid
# array([[ 10.,  10.,  10., ...,  10.,  10.,  10.],
#        [ 10.,  10.,  10., ...,  10.,  10.,  10.],
#        [ 10.,  10.,  10., ...,  10.,  10.,  10.],
#        ...,
#        [ 10.,  10.,  10., ...,  10.,  10.,  10.],
#        [ 10.,  10.,  10., ...,  10.,  10.,  10.],
#        [ 10.,  10.,  10., ...,  10.,  10.,  10.]])

# >>> a = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
# >>> a
# array([[ 1,  2,  3,  4],
#        [ 5,  6,  7,  8],
#        [ 9, 10, 11, 12]])
# 1行
# >>> a[1]
# array([5, 6, 7, 8])
# 1列
# >>> a[:,1]
# array([ 2,  6, 10])

# >>> a[1:3, 1:3]
# array([[ 6,  7],
#        [10, 11]])
# >>> a[1:3, 1:3] += 10
# >>> a[1:3, 1:3]
# array([[16, 17],
#        [20, 21]])

# >>> np.where(a<10, a, 10)
# array([[ 1,  2,  3,  4],
#        [ 5, 10, 10,  8],
#        [ 9, 10, 10, 10]])

# 3.10 ## 矩阵
# >>> m = np.matrix([[1, -2, 3], [0, 4, 5], [7, 8, -9]])
# >>> m
# matrix([[ 1, -2,  3],
#         [ 0,  4,  5],
#         [ 7,  8, -9]])
# 转置矩阵
# >>> m.T
# matrix([[ 1,  0,  7],
#         [-2,  4,  8],
#         [ 3,  5, -9]])
# 倒转矩阵
# >>> m.I
# matrix([[ 0.33043478, -0.02608696,  0.09565217],
#         [-0.15217391,  0.13043478,  0.02173913],
#         [ 0.12173913,  0.09565217, -0.0173913 ]])


# 3.11 ## 随机数
import random
# 随机选一个
# >>> values = [1,2,3,4,5]
# >>> random.choice(values)
# 4
# >>> random.choice(values)
# 1
# 随机选几个
# >>> random.sample(values, 3)
# [3, 5, 1]
# 随机选择整数
# >>> random.randint(0, 10)
# 6
# 随机选float
# >>> random.random()
# 0.6558206614919974
# 随机选N位的大整数
# >>> random.getrandbits(200)
# 140521926071764574126468065759806280057355493707224074737086
# 不要用于跟密码相关的，这是伪随机数，用ssl.RAND_bytes()代替


# 3.12 时间转换
from datetime import timedelta, datetime
a = datetime(2013, 3, 1)
b = datetime(2013, 2, 28)
print(a-b)
# 1 day, 0:00:00
print((a-b).days)
# 1
# 如果要加月
from dateutil.relativedelta import relativedelta
# >>> a = datetime(2012, 9, 23)
# >>> a + relativedelta(months=+1)
# datetime.datetime(2012, 10, 23, 0, 0)
# >>> a + relativedelta(months=+4)
# datetime.datetime(2013, 1, 23, 0, 0)
# 比较之后也可得月
# >>> b = datetime(2012, 12, 21)
# >>> d = relativedelta(b, a)
# >>> d.months
# 2
# >>> d.days
# 28
# >>> d.minutes
# 0


# 3.13 ##上周五的日期
from dateutil.relativedelta import relativedelta
from dateutil.rrule import *
d = datetime.now()
print(d)
# 2014-12-06 17:04:24.502803
print(d + relativedelta(weekday=FR))
# 2014-12-12 17:04:55.823392 下个周五
print(d + relativedelta(weekday=FR(-1)))
# 2014-12-05 17:05:23.936178 上个周五


# 3.14 ## 当月的date range
from datetime import date
import calendar

def get_month_range(start_date=None):
    if start_date is None:
        start_date = date.today().replace(day=1)
        _, days_in_month = calendar.monthrange(start_date.year, start_date.month)
        # 0, 31
        end_date = start_date + timedelta(days=days_in_month)
        return (start_date, end_date)
a_day = timedelta(days=1)
first_day, last_day = get_month_range()
while first_day < last_day:
    print(first_day)
    first_day += a_day
# 2014-12-01
# 2014-12-02
# 2014-12-03
# 2014-12-04
# 2014-12-05
# 2014-12-06
# ...
# 2014-12-31

# 另一种方法：
def date_range(start, stop, step):
    while start < stop:
        yield start
        start += step

for d in date_range(datetime(2014,12,12), datetime(2014, 12, 13), timedelta(hours=6)):
    print(d)
# 2014-12-12 00:00:00
# 2014-12-12 06:00:00
# 2014-12-12 12:00:00
# 2014-12-12 18:00:00


# 3.15 ## 字符串转datetime
# strptime 效率不是很高
# 可以用这种代替:
def parse_ymd(s):
    year_s, month_s, day_s = s.split('-')
    return datetime(int(year_s), int(month_s), int(day_s))

# 3.16 ## 时区
from pytz import timezone
import pytz
d = datetime.now()
print(d)
# 2014-12-06 17:31:24.267926

central = timezone('US/Central')
loc_d = central.localize(d)
print(loc_d)
# 2014-12-06 17:33:25.684649-06:00

# 印度加尔各答时间
band_d = loc_d.astimezone(timezone('Asia/Kolkata'))
print(band_d)
# 2014-12-07 05:04:54.805397+05:30

later = central.normalize(loc_d + timedelta(minutes=30))
print(later)
# 2014-12-06 18:09:48.617389-06:00

# UTC时间
utc_d = loc_d.astimezone(pytz.utc)
print(utc_d)
# 2014-12-06 23:39:48.617389+00:00

# 得到时区名：
# >>> pytz.country_timezones('CN')
# ['Asia/Shanghai', 'Asia/Urumqi']
# >>> pytz.country_timezones('IN')
# ['Asia/Kolkata']