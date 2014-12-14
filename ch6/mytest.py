class People:
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

    def __call__(self, xx):
        print("{} -- {}".format(self.name, xx))

p1 = People('chhaya', 12, 'M')

p1('haohao')
# chhaya -- haohao