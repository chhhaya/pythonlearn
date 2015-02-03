class Person:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError('Expected a string')
        self._name = value

    @name.deleter
    def name(self):
        raise AttributeError(' can not delete')

class SubPerson(Person):
    @property
    def name(self):
        print('Getting name')
        return super().name

    @name.setter
    def name(self, value):
        print('setting name to', value)
        super(SubPerson, SubPerson).name.__set__(self, value)

    @name.deleter
    def name(self):
        print('delete value')
        super(SubPerson, SubPerson).name.__delete__(self)

s = SubPerson('Guido')
print(s.name)
s.name = 'Larry'
# s.name = 42

# 只改getter
class SubbPerson(Person):
    @Person.name.getter
    def name(self):
        print('get name')
        return super().name

sbp = SubbPerson('xxx')
print(sbp.name)
sbp.name = 'xxxxxx'
# sbp.name = 33
print(sbp.name)

# 只改setter
class SubbPersonn(Person):
    @Person.name.setter
    def name(self, value):
        print('setting name to', value)
        super(SubbPersonn, SubbPersonn).name.__set__(self, value)

