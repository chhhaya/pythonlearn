# coding:utf8
from io import StringIO
import unittest
from unittest import TestCase
from unittest.mock import patch
import mymodule

"""
Problem: 有个程序只输出到标准输出(sys.stdout), 要测试这个输出是否正确
Solution: 一般的测试都是测试返回值，这个没有返回值，用mock.patch函数，来获得这个输出，再跟预期比对
"""

class TestURLPrint(TestCase):
    def test_url_gets_to_stdout(self):
        protocol = 'http'
        host = 'www'
        domain = 'example.com'
        expected_url = '{}://{}.{}\n'.format(protocol, host, domain)

        with patch('sys.stdout', new=StringIO()) as fake_out:
            mymodule.urlprint(protocol, host, domain)
            self.assertEqual(fake_out.getvalue(), expected_url)

if __name__ == '__main__':
    unittest.main(verbosity=1)                              