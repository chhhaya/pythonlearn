# 另一种用继承的方法

class Connection:
    def __init__(self):
        self.new_state(ClosedConnection)

    def new_state(self, newstate):
        self.__class__ = newstate

    def read(self):
        raise NotImplementedError()

    def write(self, data):
        raise NotImplementedError()

    def open(self):
        raise NotImplementedError()

    def close(self):
        raise NotImplementedError()

class ClosedConnection(Connection):
    def read(self):
        raise RuntimeError('not open')


    def write(self, data):
        raise RuntimeError('not open')


    def open(self):
        self.new_state(OpenConnection)


    def close(self):
        raise RuntimeError('already close')

class OpenConnection(Connection):
    def read(self):
        print('reading')


    def write(self, data):
        print('writing')


    def open(self):
        raise RuntimeError('already open')


    def close(self):
        self.new_state(ClosedConnection)

c = Connection()
print(c)
# <class '__main__.ClosedConnectionState'>
# c.read()
# RuntimeError: not open
c.open()
print(c)
# <class '__main__.OpenConnectionState'>
c.read()
# reading
c.write('xx')
# writing
c.close()
print(c)
# <class '__main__.ClosedConnectionState'>
