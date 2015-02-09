# 就是反射嘛

import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return 'Point({!r:} {!r:})'.format(self.x, self.y)

    def distance(self, x, y):
        return math.hypot(self.x - x, self.y - y)

p = Point(2, 3)
d = getattr(p, 'distance')(1, 1)
print(d)
# 2.23606797749979

# 方法二：
import operator

d = operator.methodcaller('distance', 0, 0)(p)
print(d)
# 3.605551275463989


# 计算到原点的距离
points = [
    Point(5, 6),
    Point(2, 3),
    Point(3, 4),
    Point(4, 5),
    Point(5, 6)
]
points.sort(key=operator.methodcaller('distance', 0, 0))
print(points)
# [Point(2 3), Point(3 4), Point(4 5), Point(5 6), Point(5 6)]
