class BraceMessage:
    def __init__(self, fmt, *args, **kwargs):
        self.fmt = fmt
        self.args = args
        self.kwargs = kwargs

    def __str__(self):
        return self.fmt.format(*self.args, **self.kwargs)

class DollarMessage:
    def __init__(self, fmt, **kwargs):
        self.fmt = fmt
        self.kwargs = kwargs

    def __str__(self):
        from string import Template
        return Template(self.fmt).substitute(**self.kwargs)

class Point:
    pass

print(BraceMessage('Message with {0} {name}', 2, name='placeholders'))
p = Point()
p.x = 0.5
p.y = 0.2
print(BraceMessage('Message with coordinates: ({point.x: .2f}, {point.y: .2f})', point=p))
print(DollarMessage('Message with $num $what', num=2, what='placeholders'))

