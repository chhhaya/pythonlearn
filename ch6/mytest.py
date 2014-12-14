class People:
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

p1 = People('chhaya', 12, 'M')
print(vars(p1))
# {'age': 12, 'name': 'chhaya', 'sex': 'M'}
print(type(p1).__name__)
# People