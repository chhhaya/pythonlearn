import unittest
import errno

def parse_int(s):
    x = int(s)
    return x

class TestConversion(unittest.TestCase):
    def test_bad_int(self):
        """
        所测试的函数必须有异常
        :return:
        """
        self.assertRaises(ValueError, parse_int, 'a')

    def test_bad_int2(self):
        """
        不使用assertRaises的情况， 还需要额外检查其他异常情况， 如test_bad_int3
        :return:
        """
        try:
            r = parse_int('A')
        except ValueError as e:
            self.assertEqual(type(e), ValueError)

    def test_bad_int3(self):
        try:
            r = parse_int('a')
        except ValueError as e:
            self.assertEqual(type(e), ValueError)
        else:
            self.fail('ValueError not raised')

    def test_bad_int4(self):
        """
        带检查异常内容的
        :return:
        """
        self.assertRaisesRegex(ValueError, 'invalid literal .*', parse_int, 'a')

    def test_bad_int5(self):
        """
        可以用context manager
        :return:
        """
        with self.assertRaisesRegex(ValueError, 'invalid literal .*'):
            r = parse_int('a')

    def test_file_not_found(self):
        """
        所测试的函数的异常的详细信息
        :return:
        """
        try:
            f = open('/file/not/found')
        except IOError as e:
            self.assertEqual(e.errno, errno.ENOENT)
        else:
            self.fail('IOError not raised')


unittest.main(verbosity=2)