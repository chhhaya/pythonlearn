def example():
    try:
        int('N/A')
    except ValueError as e:
        raise RuntimeError('A parsing error') from e


try:
    example()
except RuntimeError as e:
    print('it didn\'t work:', e)
    if e.__cause__:
        print('Cause:', e.__cause__)

# it didn't work: A parsing error
# Cause: invalid literal for int() with base 10: 'N/A'

# 会打印出两种异常
def example2():
    try:
        int('N')
    except ValueError as e:
        print('could\'t parse:', err)
# example2()

# 不打印内部异常
def example3():
    try:
        int('N')
    except ValueError:
        raise RuntimeError('A parsing error') from None
example3()

# 用raise的时候最好加上from, 外部捕捉到的异常会更清晰
try:
    ...
except SomeException as e:
    raise DifferentException() from e

