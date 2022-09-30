import sys

sys.path.insert(0, './src')

import module_quality as mq
import unittest

def setUpModule():
    print('\nExecuting SetUpModule')

def tearDownModule():
    print('\nExecuting TearDownModule')

class TestModuleQuality(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print('\nExecuting SetUpClass')

    @classmethod
    def tearDownClass(cls):
        print('\nExecuting TearDownClass')

    def setUp(self):
        print('\nExecuting SetUpMethod')

    def tearDown(self):
        print('\nExecuting TearDownMethod')
        
    def test_case_ints_positive_positive(self):
        print('\nExecuting Case Test: Integers - Positive - Positive')
        self.assertEqual(mq.simplest_func(1, 1), 2)

    def test_case_ints_negative_negative(self):
        print('\nExecuting Case Test: Integers - Negative - Negative')
        self.assertEqual(mq.simplest_func(-1, -1), -2)

    def test_case_floats_positive_positive(self):
        print('\nExecuting Case Test: Floats - Positive - Positive')
        self.assertAlmostEqual(mq.simplest_func(1.0, 1.5), 2.5, 5)

    def test_case_floats_negative_negative(self):
        print('\nExecuting Case Test: Floats - Negative - Negative')
        self.assertAlmostEqual(mq.simplest_func(-1.0, -1.5), -2.5, 5)

# try:
#     print(mq.simplest_func(1, 'Hello, world!'))
# except AssertionError as error:
#     print('Invalid arguments!', error)

# print(mq.simplest_func(1, -1))

# print(mq.simplest_func(1, 1.0))

# print(mq.simplest_func(-1.0, 1.0))

if __name__ == '__main__':
    unittest.main(verbosity=2)