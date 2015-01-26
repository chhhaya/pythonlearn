# 必须带keyword的参数

def recv(maxsize, *, block):
    'Receives a message'
    pass

recv(1024, block=True)  # OK
# recv(1024, True)  # TypeError


def mininum(*values, clip=None):
    m = min(values)
    if clip is not None:
        m = clip if clip > m else m
    return m

print(mininum(1, 5, 2, -5, 10))
# -5
print(mininum(1, 5, 2, -5, 10, clip=0))
# 0