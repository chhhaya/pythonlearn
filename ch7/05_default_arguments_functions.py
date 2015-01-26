_no_value = object()
def spam(a, b=_no_value):
    if b is _no_value:
        print('No b value supplied')
    return b

spam(1)
# No b value supplied
spam(1, 2)
spam(1, None)


# 默认值是变量的话，只生效一次
x = 42
def spam(a,b=x):
    print(a, b)

spam(1)
# 1 42
x = 43
spam(1)
# 1 42


# 默认值只传None, True,False, numbers, string这些，不要放[]这些
# 因为[]的值会被改
# 判断是否是None 用 is None来判断！！
