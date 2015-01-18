"""
Problem： 处理多种异常
"""

# # 可以一锅端
try:
    client_obj.get_url(url)
except (URLError, ValueError, SocketTimeout)
    client_obj.remove_url()

# # 可以一个一个捉
try:
    client_obj.get_url(url)
except (URLError, ValueError):
    client_obj.remove_url()
except SocketTimeout:
    client_obj.handle_url_timeout(url)


# # 可以根据errno判断
import errno
import logging
try:
    f = open(filename)
except OSError as e:
    if e.errno == errno.ENOENT:
        logging.error('File not fount')
    elif e.errno == errno.EACCES:
        logging.error('Perm deny')
    else:
        logging.error('Unexpected error')

# # # 查看继承关系：
FileNotFoundError.__mro__
# (<class 'FileNotFoundError'>, <class 'OSError'>, <class 'Exception'>, <class 'BaseException'>, <class 'object'>)
