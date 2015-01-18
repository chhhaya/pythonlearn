from unittest.mock import patch
import unittest
import mymodule

"""
Problem: 测试某些对象是如何使用的，（使用了某些参数，访问了某些属性）
Solution: patch() 可以作为装饰器， context manager或者独立
"""

class MyTestCase(unittest.TestCase):

    @patch('mymodule.func')
    def test1(self, mock_func):
        x = 1
        mymodule.func(x)
        mock_func.assert_called_with(x)

    def test2(self):
        x = 1
        with patch('mymodule.func') as mock_func:
            mymodule.func(x)
            mock_func.assert_called_with(x)

    def test3(self):
        x = 1
        p = patch('mymodule.func')
        mock_func = p.start()
        mymodule.func(x)
        mock_func.assert_called_with(x)
        p.stop()

# # patch() 把一个存在的对象用一个新的值替换了，默认是magicMock
# >>> x = 42
# >>> with patch('__main__.x'):
# 	print(x)
#
# <MagicMock name='x' id='4388942344'>

# # 也可以自己指定
# >>> with patch('__main__.x', 'patched_value'):
# 	print(x)
#
# patched_value

# # MagicMock实例用于替换callable和实例，
# >>> from unittest.mock import MagicMock
# >>> m = MagicMock(return_value=10)
# >>> m(1, 2, debug=True)
# 10
# >>> m.assert_called_with(1, 2, debug=True)
# >>> m.assert_called_with(1, 2)
# Traceback (most recent call last):
#   File "<pyshell#17>", line 1, in <module>
#     m.assert_called_with(1, 2)
#   File "/Library/Frameworks/Python.framework/Versions/3.4/lib/python3.4/unittest/mock.py", line 771, in assert_called_with
#     raise AssertionError(_error_message()) from cause
# AssertionError: Expected call: mock(1, 2)
# Actual call: mock(1, 2, debug=True)

# >>> m.upper.return_value = 'HELLO'
# >>> m.upper('hello')
# 'HELLO'
# >>> assert m.upper.called

# >>> m.split.return_value = ['hello', 'world']
# >>> m.split('hello world')
# ['hello', 'world']
# >>> m.split.assert_called_with('hello world')

# >>> m['blam']
# <MagicMock name='mock.__getitem__()' id='4327874856'>
# >>> m.__getitem__.called
# True
# >>> m.__getitem__.assert_called_with('blah')
# Traceback (most recent call last):
#   File "<pyshell#28>", line 1, in <module>
#     m.__getitem__.assert_called_with('blah')
#   File "/Library/Frameworks/Python.framework/Versions/3.4/lib/python3.4/unittest/mock.py", line 771, in assert_called_with
#     raise AssertionError(_error_message()) from cause
# AssertionError: Expected call: __getitem__('blah')
# Actual call: __getitem__('blam')
# >>> m.__getitem__.assert_called_with('blam')


# # 要测试的函数需要从网上下载东西，但是要在离线的环境下测试
# # 用io.BytesIO替换了urlopen操作
import io
sample_data = io.BytesIO(b'''\
"IBM", 91.1\r
"AA", 13.12\r
"MSFF", 23.22\r
\r
''')
class Tests(unittest.TestCase):
    @patch('mymodule.urlopen', return_value=sample_data)
    def test_dowprices(self, mock_urlopen):
        p = mymodule.dowprices()
        self.assertTrue(mock_urlopen.called)
        self.assertEqual(p, {'IBM': 91.1, 'AA': 13.12, 'MSFF': 23.22})

unittest.main(verbosity=2)






















