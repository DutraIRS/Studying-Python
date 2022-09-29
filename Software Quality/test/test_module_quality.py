import sys

sys.path.insert(0, '../src')

import module_quality as mq
import unittest

try:
    print(mq.simplest_func(1, 'Hello, world!'))
except AssertionError as error:
    print('Invalid arguments!', error)

print(mq.simplest_func(1, -1))

print(mq.simplest_func(1, 1.0))

print(mq.simplest_func(-1.0, 1.0))

if __name__ == '__main__':
    unittest.main(verbosity=2)