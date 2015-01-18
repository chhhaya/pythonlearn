# 定义，要从内置Exception继承
# 但是不要继承BaseException
class NetworkError(Exception):
    pass

class HostnameError(NetworkError):
    pass

class TimeoutdError(NetworkError):
    pass

class ProtocolError(NetworkError):
    pass


# 使用
try:
    msg = s.recv()
except TimeoutdError as e:
    ...
except ProtocolError as e:
    ...


# 自定义参数的
class CustomError(Exception):
    def __init__(self, message, status):
        super().__init__(message, status)
        self.message = message
        self.status = status

try:
    raise CustomError('haha', 2)
except CustomError as e:
    print(e.args)
    print(e.message, e.status)

#
# ('haha', 2)
# ’haha' 2