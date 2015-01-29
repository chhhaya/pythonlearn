class Pair:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return 'Pair({0.x!r}, {0.y!r})'.format(self)

    def __str__(self):
        return '({0.x!s}, {0.y!s})'.format(self)

# '{0.x}'.format(self)  表示第一个参数的x属性
# 也可以写成 '%r' % self.x

p = Pair(3, 4)
print(p)
# (3, 4)
print(repr(p))
# Pair(3, 4)