import unittest

"""
Problem: 测试结果要保存到文件中，而不是输出来
"""

import sys

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

def main(out=sys.stderr, verbosity=2):
    # testLoader实例用于组装一个test suite
    loader = unittest.TestLoader()
    # 从当前文件载入test suite
    suite = loader.loadTestsFromModule(sys.modules[__name__])
    # 这是main()的一个更底层的用法，可以指定输出
    unittest.TextTestRunner(out, verbosity=verbosity).run(suite)

if __name__ == '__main__':
    with open('testing.out', 'w') as f:
        main(f, verbosity=2)
