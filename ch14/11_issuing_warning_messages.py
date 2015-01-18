import warnings

def func(x, y, logfile=None, debug=False):
    if logfile is not None:
        warnings.warn('logfile argument deprecated', DeprecationWarning)

func(1, 2, 'log.txt')

# 运行方法
# alpha$ python -W all 11_issuing_warning_messages.py
# 11_issuing_warning_messages.py:5: DeprecationWarning: logfile argument deprecated
#   warnings.warn('logfile argument deprecated', DeprecationWarning)

# 异常形式：
# alpha$ python -W error 11_issuing_warning_messages.py
# Traceback (most recent call last):
#   File "11_issuing_warning_messages.py", line 7, in <module>
#     func(1, 2, 'log.txt')
#   File "11_issuing_warning_messages.py", line 5, in func
#     warnings.warn('logfile argument deprecated', DeprecationWarning)
# DeprecationWarning: logfile argument deprecated

# -W 选项可控制warning消息的输出
# -W all: 所有消息
# -W ignore: 忽略所有warning
# -W error: 所有warning转为Exception
#
# 也可以用simplefilter来控制
# always：所有输出
# ignore：不输出
# error：转为exception

import warnings
warnings.simplefilter('always')
f = open('/etc/passwd')
del f

# Warning (from warnings module):
#   File "__main__", line 1
# ResourceWarning: unclosed file <_io.TextIOWrapper name='/etc/passwd' mode='r' encoding='US-ASCII'>
