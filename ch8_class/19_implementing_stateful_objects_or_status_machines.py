class Connection:
    def __init__(self):
        self.new_state(ClosedConnectionState)

    def new_state(self, newstate):
        self._state = newstate

    def read(self):
        self._state.read(self)

    def write(self, data):
        self._state.write(self, data)

    def open(self):
        self._state.open(self)

    def close(self):
        self._state.close(self)

class ConnectionState:
    @staticmethod
    def read(conn):
        raise NotImplementedError()

    @staticmethod
    def write(conn, data):
        raise NotImplementedError()

    @staticmethod
    def open(conn):
        raise NotImplementedError()

    @staticmethod
    def close(conn):
        raise NotImplementedError()

class ClosedConnectionState(ConnectionState):
    @staticmethod
    def read(conn):
        raise RuntimeError('not open')

    @staticmethod
    def write(conn, data):
        raise RuntimeError('not open')

    @staticmethod
    def open(conn):
        conn.new_state(OpenConnectionState)

    @staticmethod
    def close(conn):
        raise RuntimeError('already close')

class OpenConnectionState:
    @staticmethod
    def read(conn):
        print('reading')

    @staticmethod
    def write(conn, data):
        print('writing')

    @staticmethod
    def open(conn):
        raise  RuntimeError('already open')

    @staticmethod
    def close(conn):
        conn.new_state(ClosedConnectionState)

c = Connection()
print(c._state)
# <class '__main__.ClosedConnectionState'>
# c.read()
# RuntimeError: not open
c.open()
print(c._state)
# <class '__main__.OpenConnectionState'>
c.read()
# reading
c.write('xx')
# writing
c.close()
print(c._state)
# <class '__main__.ClosedConnectionState'>
