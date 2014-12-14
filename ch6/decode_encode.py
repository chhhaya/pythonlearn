s = b'hello'
import binascii
# 字节字符串-》十六进制
h = binascii.b2a_hex(s)
print(h)
# b'68656c6c6f'
# 十六进制 -> 字节字符串
print(binascii.a2b_hex(h))
# b'hello'

# 用base64里的b16一样的
import base64
h = base64.b16encode(s)
print(h)
print(base64.b16decode(h))
# b'68656C6C6F'  # 大写
# b'hello'
print(h.decode('ascii'))
# 68656C6C6F  # 不带b的

### base64
a = base64.b64encode(s)
print(a)
# b'aGVsbG8='
print(base64.b64decode(a))
# b'hello'


### 二进制数组结构
from struct import Struct
# 写
def write_records(records, format, f):
    record_struct = Struct(format)
    for r in records:
        f.write(record_struct.pack(*r))
records = [(1, 2.3, 4.5),
    (2, 3.4, 3.4),
    (5, 4.3, 8.9)]
# with open('data.b', 'wb') as f:
#     write_records(records, '<idd', f)

# 读
def read_records(format, f):
    record_struct = Struct(format)
    chunks = iter(lambda: f.read(record_struct.size), b'')
    return(record_struct.unpack(chunk) for chunk in chunks)

with open('data.b', 'rb') as f:
    for rec in read_records('<idd', f):
        print(rec)

# 读2
def unpack_records(format, data):
    record_struct = Struct(format)
    return(record_struct.unpack_from(data, offset) for offset in range(0, len(data), record_struct.size))

with open('data.b', 'rb') as f:
    data = f.read()
    for rec in unpack_records('<idd', data):
        print(rec)

record_struct = Struct('<idd')
print(record_struct.size)
# 20
print(record_struct.pack(1, 2.0, 3.0))
# b'\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00@\x00\x00\x00\x00\x00\x00\x08@'
print(record_struct.unpack(b'\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00@\x00\x00\x00\x00\x00\x00\x08@'))
# (1, 2.0, 3.0)

# 也可以：
import struct
print(struct.pack('<idd', 1, 2.0, 3.0))
print(struct.unpack('<idd', b'\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00@\x00\x00\x00\x00\x00\x00\x08@'))

# 使用生成器，每次读固定大小的数据
with open('data.b', 'rb') as f:
    chunks = iter(lambda: f.read(20), b'')
    # <callable_iterator object at 0x101985be0>
    print(chunks)
    for chk in chunks:
        print(chk)
    # b'\x01\x00\x00\x00ffffff\x02@\x00\x00\x00\x00\x00\x00\x12@'
    # b'\x02\x00\x00\x00333333\x0b@333333\x0b@'
    # b'\x05\x00\x00\x00333333\x11@\xcd\xcc\xcc\xcc\xcc\xcc!@'

def read_recordss(format, f):
    record_struct = Struct(format)
    while True:
        chk = f.read(record_struct.size)
        if chk == b'':
            break
        yield record_struct.unpack(chk)
    return records

print('--'*10)
# 使用namedtuple
from collections import namedtuple
Record = namedtuple('Record', ['kind', 'x', 'y'])
fz = open('data.b', 'rb')
records = (Record(*r) for r in read_recordss('<idd', fz))
f.close()
for r in records:
    print(r.kind, r.x, r.y)
# 1 2.3 4.5
# 2 3.4 3.4
# 5 4.3 8.9


# 如果要读大量数据，最好用numpy
import numpy as np
f = open('data.b', 'rb')
records = np.fromfile(f, dtype='<i, <d, <d')
print(records)
# [(1, 2.3, 4.5) (2, 3.4, 3.4) (5, 4.3, 8.9)]
# 其他的如果是图片，shapefile等，最好先找找有没有库，以免重复造轮子