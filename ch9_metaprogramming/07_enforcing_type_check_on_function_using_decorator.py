from inspect import signature
from functools import wraps

def typeassert(*ty_args, **ty_kwargs):
    def decorate(func):
        if not __debug__:
            return func

        sig = signature(func)  # #?
        bound_types = sig.bind_partial(*ty_args, **ty_kwargs).arguments

        @wraps(func)
        def wrapper(*args, **kwargs):
            bound_values = sig.bind(*args, **kwargs)
            for name, value in bound_values.arguments.items():
                if name in bound_types:
                    if not isinstance(value, bound_types[name]):
                        raise TypeError(
                            'Arument {} must be {}'.format(name, bound_types[name])
                        )
            return func(*args, **kwargs)
        return wrapper
    return decorate

@typeassert(int, int)
def add(x, y):
    return x+y

add(1, 2)
# add(1, '2')
# TypeError: Arument y must be <class 'int'>


# signature的用法

def spam(x, y, z=42):
    pass

sig = signature(spam)
print(sig)
# (x, y, z=42)
print(sig.parameters)
# OrderedDict([('x', <Parameter at 0x101a54fc0 'x'>), ('y', <Parameter at 0x101a54e58 'y'>), ('z', <Parameter at 0x101a54f78 'z'>)])
print(sig.parameters['z'].name)
# z
print(sig.parameters['z'].default)
# 42
print(sig.parameters['z'].kind)
# POSITIONAL_OR_KEYWORD


# signature的partial_bind
bound_types = sig.bind_partial(int, z=int)
print(bound_types)
# <inspect.BoundArguments object at 0x1005a1908>
print(bound_types.arguments)
# OrderedDict([('x', <class 'int'>), ('z', <class 'int'>)])

# signature的bind 就是完整的,不能缺参数的
bound_values = sig.bind(1, 2, 3)
print(bound_values.arguments)
# OrderedDict([('x', 1), ('y', 2), ('z', 3)])
