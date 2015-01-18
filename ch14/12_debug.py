# alpha$ python -i sample.py
# Traceback (most recent call last):
#   File "sample.py", line 4, in <module>
#     func('Hello')
#   File "sample.py", line 2, in func
#     return n+10
# TypeError: Can't convert 'int' object to str implicitly
# >>> func(10)
# 20
# 可以调试
# >>> import pdb
# >>> pdb.pm()

## 打印出异常堆栈
from sample import func
import traceback
import sys
try:
    func('hel')
except:
    print('Error')
    traceback.print_exc(file=sys.stderr)


## 打印堆栈
def samp(n):
    if n > 0:
        samp(n-1)
    else:
        traceback.print_stack(file=sys.stderr)
samp(5)
