# 运行时绑定
# >>> x = 10
# >>> a = lambda y: x+y
# >>> x = 20
# >>> b = lambda y:x+y
# >>> a(10)
# 30
# >>> b(10)
# 30

# 定义时绑定
# >>> x = 10
# >>> a = lambda y,x=x:x+y
# >>> x = 20
# >>> b = lambda y, x=x: x+y
# >>> a(10)
# 20
# >>> b(10)
# 30

# 运行时绑定，每次n＝4
# >>> funcs = [lambda x: x+n for n in range(5)]
# >>> for f in funcs:
# 	print(f(0))
#
#
# 4
# 4
# 4
# 4
# 4

# 定义时绑定，n为0，1，2，3，4
# >>> funcs = [lambda x, n=n: x+n for n in range(5)]
# >>> for f in funcs:
# 	print(f(0))
#
#
# 0
# 1
# 2
# 3
# 4