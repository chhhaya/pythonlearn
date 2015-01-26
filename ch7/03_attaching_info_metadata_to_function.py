def add(x:int, y:int) -> int:
    return x+y

help(add)
# add(x:int, y:int) -> int

print(add.__annotations__)
# {'y': <class 'int'>, 'x': <class 'int'>, 'return': <class 'int'>}

